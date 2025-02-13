# Generator Dates

Generator Dates — это Python-библиотека для генерации случайных дат в различных форматах и языках.  
Поддерживает английский (`en`) и русский (`ru`) языки.

## Возможности

- Генерация случайных дат с настраиваемым форматом
- Поддержка полного и сокращенного названий месяцев
- Выбор диапазона дней, месяцев и годов

## Установка

Установить можно через `pip` (после публикации на PyPI):

```sh
pip install generator_dates
```

Или вручную:

```sh
git clone https://github.com/yourusername/generator_dates.git
cd generator_dates
pip install .
```

## Использование

```python
from generator_dates import GeneratorDates

generator = GeneratorDates(format="{d} {month} {y}", lang="ru")
random_date = generator.generate_date()
print(random_date)  # Например: 12 марта 1987
```

## Настройки

- **`format`** – строка формата даты:
  - `{d}` – день месяца
  - `{m}` – число месяца
  - `{y}` – год
  - `{mon}` – сокращенное название месяца
  - `{month}` – полное название месяца
- **`lang`** – язык (`en` или `ru`)

## Лицензия

Проект распространяется под лицензией MIT.
