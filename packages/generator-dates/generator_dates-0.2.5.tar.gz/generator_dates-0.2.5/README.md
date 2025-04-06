"""
# Generator Dates

Generator Dates is a Python library for generating random dates in various formats and languages.  
Supports English (`en`) and Russian (`ru`) languages.

## Features

- Random date generation with a customizable format
- Support for full and abbreviated month names
- Selection of day, month, and year ranges
- Saving history of generated dates
- Output support as `datetime` and `date` objects
- Handling of invalid ranges

## Installation

Install via `pip`:

```sh
pip install generator_dates
```

Or manually:

```sh
git clone https://github.com/yourusername/generator_dates.git
cd generator_dates
pip install .
```

## Usage

```python
from generator_dates import GeneratorDates

generator = GeneratorDates(format="{d} {month} {y}", lang="ru", save_history=True)
random_date = generator.generate_date(range_day=(1, 30), range_month=(1, 12), range_year=(1900, 2023))
print(random_date)  # Example: 12 марта 1987

# View history of generated dates
print(generator.history)
```

## Settings

- **`format`** – date format string:
  - `{d}` – day of the month
  - `{m}` – month number
  - `{y}` – year
  - `{mon}` – abbreviated month name
  - `{month}` – full month name
  - `'datetime'` – returns a `datetime` object
  - `'date'` – returns a `date` object
- **`lang`** – language (`en` or `ru`)
- **`save_history`** – whether to save the history of generated dates (default is `True`)

## Exceptions

- `LanguageError` – if an unsupported language is provided.
- `ValueError` – if invalid ranges for day, month, or year are given.

## License

This project is licensed under the MIT License.
"""