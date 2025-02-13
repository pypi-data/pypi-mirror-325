import string
from typing import Any, Callable, Dict, List, Optional

from aigoo_fusion.chat.messages.message import Message
from aigoo_fusion.chat.messages.message_temp import MessageTemp
from aigoo_fusion.chat.messages.role import Role
from aigoo_fusion.chat.models.base_ai_model import BaseAIModel
from aigoo_fusion.chat.responses.chat_response import ChatResponse
from aigoo_fusion.chat.tools.tool import Tool
from aigoo_fusion.exception.aigoo_exception import AIGooException

class AIGooChat:
	def __init__(
		self, 
		llm: BaseAIModel, 
		system_message: Optional[str] = None, 
		input_variables: Optional[List[str]]= None,
	):
		self.model: BaseAIModel = llm
		self.messages_temp: MessageTemp = MessageTemp()
		self.system_message = system_message
		self.input_variables = input_variables or []
		self._tools: Dict[str, Callable] = {}
		self._tool_definitions: Dict[str, Dict[str, Any]] = {}

		def _has_variable_placeholder(s):
			return bool(list(string.Formatter().parse(s)) and any(field for _, field, _, _ in string.Formatter().parse(s) if field))

		def _extract_variable_names(s):
			return list(set([field for _, field, _, _ in string.Formatter().parse(s) if field]))

		# Validate that if system message has variable then input variable should not be empty
		if (_has_variable_placeholder(self.system_message) if self.system_message else False) and not self.input_variables:
			variable_names = _extract_variable_names(self.system_message)
			raise AIGooException(
				f"System messages have placeholder variables, so the `input variable` should not be empty. "
				f"Missing input variables: {variable_names}. "
			)

		# Validate input variables
		if self.system_message and self.input_variables:
			# Validate that all required input variables are in kwargs
			variable_names = _extract_variable_names(self.system_message)
			missing_vars = [var for var in variable_names if var not in self.input_variables]
			if missing_vars:
				raise AIGooException(
					f"Missing required input variables: {missing_vars}. "
					f"Expected variables: {variable_names}."
				)


	def register_tool(self, funcs: List[Callable]) -> None:
		"""Register a tool with this framework instance."""
		for func in funcs:
			if not hasattr(func, '_is_tool'):
				raise AIGooException("Function must be decorated with @Tool")

			tool_def = Tool._get_tool_definition(func, getattr(func, '_tool_strict', True))
			self._tools[func.__name__] = func
			self._tool_definitions[func.__name__] = tool_def


	def __get_tool_definitions(self) -> List[Dict[str, Any]]:
		"""Get all tool definitions registered with this framework."""
		return list(self._tool_definitions.values())


	def __execute_tool(self, name: str, arguments: Dict[str, Any]) -> Any:
		"""Execute a registered tool."""
		if name not in self._tools:
			raise AIGooException(f"Tool not found: {name}")
		return self._tools[name](**arguments)


	def __validate_system_message(self, **kwargs) -> (str | None):
		# If we have a system message and input variables
		try:
			final_system_message = self.system_message if self.system_message else ""
			if self.system_message and self.input_variables:
				# Validate that all required input variables are in kwargs
				missing_vars = [var for var in self.input_variables if var not in kwargs]
				if missing_vars:
					raise AIGooException(
						f"Missing required input variables: {missing_vars}. "
						f"Expected variables: {self.input_variables}, "
						f"Received variables: {list(kwargs.keys())}"
					)

				# Create a dictionary of variables from kwargs that match input_variables
				format_variables = {
					var: kwargs.get(var) 
					for var in self.input_variables 
					if var in kwargs
				}

				# Update the system message with the variables
				final_system_message = self.system_message.format(**format_variables)

			return final_system_message
		except KeyError as e:
			raise AIGooException(f"Required variable {e} not found in kwargs")
		except Exception as e:
			raise AIGooException(f"Error formatting system message: {str(e)}")


	def generate(self, messages: List[Message], **kwargs) -> ChatResponse:
		"""
		Generate a response based on a list of messages.
		
		Args:
		    messages: List of Message objects to process
		    **kwargs: Additional generation parameters
		
		Returns:
		    AIResponse containing the generated response
		"""
		try:
			self.messages_temp.clear()

			if self.system_message:
				# Validate system message
				final_system_message = self.__validate_system_message(**kwargs)

				# Add system message to history
				self.messages_temp.add_system_message(final_system_message if final_system_message else "")

			# Add new messages to history
			for message in messages:
				if message.role == Role.USER:
					self.messages_temp.add_user_message(message.content if message.content else "")
				elif message.role == Role.ASSISTANT:
					self.messages_temp.add_assistant_message(
						content=message.content,
						tool_calls=message.tool_calls
					)
				elif message.role == Role.TOOL:
					self.messages_temp.add_tool_message(
						tool_call_id=message.tool_call_id if message.tool_call_id else "",
						name=message.name if message.name else "",
						content=message.content if message.content else ""
					)

			response = self.model.generate(
				self.messages_temp.get_messages(),
				tools=self.__get_tool_definitions()
			)

			self.messages_temp.add_assistant_message(content=response.content, tool_calls=response.tool_calls)

			return ChatResponse(
				result=response,
				process=self.messages_temp.get_instance_messages()
			)
		except Exception as e:
			raise AIGooException(e)


	def generate_with_tools(self, messages: List[Message], **kwargs) -> ChatResponse:
		"""
		Generate a response based on a list of messages.
		
		Args:
		    messages: List of Message objects to process
		    **kwargs: Additional generation parameters
		
		Returns:
		    AIResponse containing the generated response
		"""
		try:
			self.messages_temp.clear()

			if self.system_message:
				# Validate system message
				final_system_message = self.__validate_system_message(**kwargs)

				# Add system message to history
				self.messages_temp.add_system_message(final_system_message if final_system_message else "")

			# Add new messages to history
			for message in messages:
				if message.role == Role.USER:
					self.messages_temp.add_user_message(message.content if message.content else "")
				elif message.role == Role.ASSISTANT:
					self.messages_temp.add_assistant_message(
						content=message.content, 
						tool_calls=message.tool_calls
					)
				elif message.role == Role.TOOL:
					self.messages_temp.add_tool_message(
						tool_call_id=message.tool_call_id if message.tool_call_id else "",
						name=message.name if message.name else "",
						content=message.content if message.content else ""
					)

			while True:
				response = self.model.generate(
					self.messages_temp.get_messages(),
					tools=self.__get_tool_definitions(),
				)

				if response.tool_calls:
					self.messages_temp.add_assistant_message(tool_calls=response.tool_calls)

					for tool_call in response.tool_calls:
						result = self.__execute_tool(
							tool_call.name,
							tool_call.arguments
						)
						self.messages_temp.add_tool_message(
							tool_call_id=tool_call.tool_call_id,
							name=tool_call.name,
							content=str(result)
						)
					continue

				self.messages_temp.add_assistant_message(content=response.content, tool_calls=response.tool_calls)

				return ChatResponse(
					result=response,
					process=self.messages_temp.get_instance_messages()
				)
		except Exception as e:
			raise AIGooException(e)

	def generate_stream(self, messages: List[Message], **kwargs) -> Any:
		"""
		Generate a streaming response based on a list of messages.
		
		Args:
		    messages: List of Message objects to process
		    **kwargs: Additional generation parameters
		
		Returns:
		    Streaming response from the model
		"""
		try:
			# Add new messages to history
			for message in messages:
				if message.role == Role.USER:
					self.messages_temp.add_user_message(message.content if message.content else "")
				elif message.role == Role.ASSISTANT:
					self.messages_temp.add_assistant_message(
						content=message.content, 
						tool_calls=message.tool_calls
					)
				elif message.role == Role.TOOL:
					self.messages_temp.add_tool_message(
						tool_call_id=message.tool_call_id if message.tool_call_id else "",
						name=message.name if message.name else "",
						content=message.content if message.content else ""
					)

			return self.model.generate_stream(
				self.messages_temp.get_messages(),
				tools=self.__get_tool_definitions(),
			)
		except Exception as e:
			raise AIGooException(e)

	def clear_messages_temp(self) -> None:
		self.messages_temp.clear()