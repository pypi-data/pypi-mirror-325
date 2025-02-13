# Ninety Codegen

A Python package for generating and validating code using OpenAI's API.

## Features
- Generate code from natural language instructions
- Validate syntax for Python, SQL, and Verilog
- Optional LLM-based code correctness validation
- Easy integration with Jupyter notebooks

## Installation

```bash
pip install ninety
```

## Quick Start

1. Set your OpenAI API key:
```python
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
```

2. Create an instructions file (`instructions.csv`):
```csv
instruction
Write a Python function to check if a number is prime
Write a Python function to find the factorial of a number
```

3. Run the pipeline:
```python
from ninety import codegen

pipeline = codegen.Pipeline(
    instructions_path="instructions.csv",
    model="gpt-4o",      # Optional: Model for generation
    syntax_check=True,   # Optional: Enable syntax validation
    language="Python",   # Optional: Target language
    samples=1           # Optional: Samples per instruction
)
pipeline.run()
```

Generated code will be saved to `output.jsonl`.

## Using Individual Components

You can also use the components separately:

```python
from ninety.codegen import CodeGenerator, SyntaxChecker, JudgeLLM

# Generate code
generator = CodeGenerator(model_name="gpt-4o")
code = generator.generate_batch(["Write a Python function to calculate the area of a circle"])[0][0]

# Check syntax
checker = SyntaxChecker()
is_valid = checker.check(code, "Python")

# Judge correctness (optional)
judge = JudgeLLM()
judgment = judge.judge("Write a Python function to calculate the area of a circle", code)
```

## Configuration Options

- `model`: OpenAI model for code generation (default: "gpt-4o")
- `syntax_check`: Enable syntax validation (default: True)
- `language`: Target programming language (default: "Python")
- `samples`: Number of samples per instruction (default: 1)

## Examples

Check out our [example.py](examples/example.py) for more detailed usage examples.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.