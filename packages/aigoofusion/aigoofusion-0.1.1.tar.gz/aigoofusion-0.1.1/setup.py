from setuptools import setup, find_packages

setup(
    name='aigoofusion', 
    version='0.1.1',
    packages=find_packages(),
    description='`AIGooFusion` is a framework for developing applications by large language models (LLMs)',
    author='irufano',
    author_email='irufano.official@gmail.com',
    url='https://github.com/irufano/aigoofusion',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)