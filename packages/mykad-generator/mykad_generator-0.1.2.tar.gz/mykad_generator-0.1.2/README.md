# MyKad Generator

A Python package to generate random Malaysian identity numbers (MyKad).

## Installation

You can install the package using Poetry:

```bash
pip install mykad_generator
```

## Usage
```bash

from mykad_generator import MyKadGenerator

generator = MyKadGenerator(num_records=5)
mykad_numbers = generator.generate_malaysia_identity_number()
print(mykad_numbers)


```
