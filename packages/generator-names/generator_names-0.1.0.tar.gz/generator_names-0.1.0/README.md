# GeneratorNames

## Overview
GeneratorNames is a Python module that generates random names based on predefined lists of first and last names. It supports both Russian and English names with gender differentiation.

## Features
- Generate random names in English and Russian.
- Supports both male and female name generation.
- Customizable output format.
- Option to save name generation history.

## Installation
```sh
pip install generator-names
```

## Usage
### Initializing the Generator
```python
from generator_names import GeneratorNames

generator = GeneratorNames(save_history=True, format='{firstname} {lastname}')
```
- `save_history` (bool): If `True`, stores generated names in history.
- `format` (str): Defines the output format using `{firstname}` and `{lastname}` placeholders. If set to `'dict'`, returns a dictionary.

### Generating Names
```python
# Generate a random male name in English
en_name = generator.generate_name(language='en', gender='male')
print(en_name)

# Generate a random female name in Russian
ru_female_name = generator.generate_name(language='ru', gender='female')
print(ru_female_name)
```
- `language` (str): `'en'` for English, `'ru'` for Russian.
- `gender` (str): `'male'` or `'female'`.

### Custom Formatting
```python
generator = GeneratorNames(format="{lastname}, {firstname}")
print(generator.generate_name(language='en'))  # Output: Doe, John
```

### Returning as Dictionary
```python
generator = GeneratorNames(format='dict')
name_dict = generator.generate_name(language='ru')
print(name_dict)  # Output: {'firstname': 'Иван', 'lastname': 'Петров'}
```

## License
This project is licensed under the MIT License.
