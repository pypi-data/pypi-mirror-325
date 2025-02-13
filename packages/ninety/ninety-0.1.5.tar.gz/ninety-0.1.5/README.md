# Ninety Codegen

A Python package for generating and validating code using OpenAI's API.

## Features
- Generate code from natural language instructions
- Validate syntax for Python, SQL, and Verilog
- Optional LLM-based code correctness validation
- Easy integration with Jupyter notebooks
- Separate models for generation and validation
- Configurable sampling parameters

## Installation

```bash
pip install ninety
```

## Quick Start

1. Set your OpenAI API key:
```python
from ninety import codegen

# Option 1: Pass API key directly
pipeline = codegen.Pipeline(
    instructions_path="instructions.csv",
    api_key="your-openai-api-key",      # Optional: Pass API key directly
    output_model="gpt-4",               # Optional: Model for code generation
    judge_model="gpt-3.5-turbo",        # Optional: Model for validation
    syntax_check=True,                  # Optional: Validate syntax and correctness
    language="Python",                  # Optional: Target language
    samples=1                          # Optional: Samples per instruction
)
pipeline.run()

# Option 2: Use environment variable
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
pipeline = codegen.Pipeline(
    instructions_path="instructions.csv"
)
pipeline.run()
```

Generated code will be saved to `output.jsonl`.

## Configuration Options

### Pipeline Parameters

- `instructions_path` (str, required): 
  - Path to CSV file containing instructions
  - CSV must have an "instruction" column

- `api_key` (str, optional): 
  - OpenAI API key for authentication
  - If not provided, will use OPENAI_API_KEY environment variable

- `output_model` (str, optional, default="gpt-3.5-turbo"): 
  - OpenAI model used for code generation
  - Recommended models: "gpt-4", "gpt-3.5-turbo"

- `judge_model` (str, optional, default="gpt-3.5-turbo"):
  - OpenAI model used for code validation
  - Can use a smaller/faster model than output_model
  - Only used if syntax_check=True

- `language` (str, optional, default="Python"):
  - Target programming language
  - Supported: "Python", "SQL", "Verilog"

- `syntax_check` (bool, optional, default=True):
  - Whether to validate syntax and correctness
  - If True, will use both static analysis and LLM validation

- `samples` (int, optional, default=1):
  - Number of code samples to generate per instruction
  - Higher values give more diverse solutions

## Using Individual Components

You can also use the components separately:

```python
from ninety.codegen import CodeGenerator, SyntaxChecker, JudgeLLM

# Generate code
generator = CodeGenerator(
    model_name="gpt-4", 
    api_key="your-openai-api-key",  # Optional
    sample_k=2,                     # Generate 2 samples
    temperature=0.7                 # Control randomness
)
code = generator.generate_batch(["Write a Python function to calculate the area of a circle"])[0][0]

# Check syntax
checker = SyntaxChecker()
is_valid = checker.check(code, "Python")

# Judge correctness
judge = JudgeLLM(model_name="gpt-3.5-turbo")
judgment = judge.judge("Write a Python function to calculate the area of a circle", code)
```

### Component Parameters

#### CodeGenerator
- `model_name` (str): OpenAI model to use
- `sample_k` (int): Number of samples per prompt
- `temperature` (float): Sampling temperature (0.0-1.0)
- `max_tokens` (int, optional): Maximum tokens to generate
- `api_key` (str, optional): OpenAI API key

#### JudgeLLM
- `model_name` (str): OpenAI model for validation
- Automatically uses API key from environment or Pipeline

#### SyntaxChecker
- Static analyzer for Python, SQL, and Verilog
- No configuration needed

## Examples

Check out our [example.py](examples/example.py) for more detailed usage examples.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.