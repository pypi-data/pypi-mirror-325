import math
from typing import Dict, List

from aigoo_fusion.chat.models.openai.openai_pricing_list import OPENAI_PRICING
from aigoo_fusion.chat.models.model_pricing import ModelPricing

class OpenAIUsage:
	"""
	OpenAIUsage class. 
	
	Count openai token usage. 
	
	Usage in `OpenAIModel`, `openai_usage_tracker` and `track_openai_usage`
	"""

	def __init__(self):
		self.total_request: int = 0
		self.output_tokens: int = 0
		self.input_tokens: int = 0
		self.total_tokens: int = 0
		self.total_cost: float = 0.0
		self.raw_usages: List[Dict[str, int]] = []
		self.pricing: Dict[str, ModelPricing] = self._load_pricing() or {}

	def __repr__(self) -> str:
		rounded_up = math.ceil(self.total_cost * 1000000) / 1000000
		return (
			f"Total Tokens: {self.total_tokens}\n"
			f"\tInput Tokens: {self.input_tokens}\n"
			f"\tOutput Tokens: {self.output_tokens}\n"
			f"Total Requests: {self.total_request}\n"
			f"Total Cost (USD): ${rounded_up:.6f}"
		)

	def _load_pricing(self) -> Dict[str, ModelPricing]:
		"""
		Load openai pricing from dictionary.
		"""
		# Price per 1M tokens for different models (USD)
		# https://platform.openai.com/docs/pricing
		pricing_data = OPENAI_PRICING
		return {
			model: ModelPricing(
				token_input=data['input'],
				token_output=data['output']
			)
			for model, data in pricing_data.items()
			}


	def update(self, model: str, usage: Dict[str, int]) -> None:
		"""
		Update usage statistics and calculate price.
		
		Args:
		    model: Model name
		    usage: Dictionary containing token counts
		"""
		ONE_MILLION = 1000000

		self.raw_usages.append(usage)
		usage_dict = vars(usage) if hasattr(usage, '__dict__') else usage
		self.total_request += 1
		self.input_tokens += usage_dict.get("prompt_tokens", 0)
		self.output_tokens += usage_dict.get("completion_tokens", 0)
		self.total_tokens = self.input_tokens + self.output_tokens

		# Calculate price
		if model in self.pricing:
			price_info = self.pricing[model]
			input_price = (self.input_tokens / ONE_MILLION) * price_info.token_input
			output_price = (self.output_tokens / ONE_MILLION) * price_info.token_output
			self.total_cost = input_price + output_price
		pass

	def reset(self):
		"""
		Reset usage statistics and calculate price.
		"""
		self.total_request = 0
		self.input_tokens = 0
		self.output_tokens = 0
		self.total_tokens = 0
		self.total_cost = 0.0
		self.raw_usages = []
