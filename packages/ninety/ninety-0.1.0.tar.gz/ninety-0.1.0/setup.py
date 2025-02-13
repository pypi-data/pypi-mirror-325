from setuptools import setup, find_packages

setup(
    name="ninety",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "pandas>=1.3.0",
        "pyverilog>=1.3.0",
        "sqlparse>=0.4.0",
        "tqdm>=4.65.0",
        "python-dotenv>=1.0.0",
    ],
    author="90x AI",
    description="A scalable pipeline for generating and validating structured code outputs",
    python_requires=">=3.8",
)
