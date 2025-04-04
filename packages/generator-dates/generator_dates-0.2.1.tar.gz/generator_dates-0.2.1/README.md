# Generator Dates

Generator Dates — это Python-библиотека для генерации случайных дат в различных форматах и языках.  
Поддерживает английский (`en`) и русский (`ru`) языки.

## Возможности

- Генерация случайных дат с настраиваемым форматом
- Поддержка полного и сокращенного названий месяцев
- Выбор диапазона дней, месяцев и годов
- Сохранение истории сгенерированных дат
- Поддержка вывода в виде объектов `datetime` и `date`
- Обработка некорректных диапазонов

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

generator = GeneratorDates(format="{d} {month} {y}", lang="ru", save_history=True)
random_date = generator.generate_date(range_day=(1, 30), range_month=(1, 12), range_year=(1900, 2023))
print(random_date)  # Например: 12 марта 1987

# Просмотр истории сгенерированных дат
print(generator.history)
```

## Настройки

- **`format`** – строка формата даты:
  - `{d}` – день месяца
  - `{m}` – число месяца
  - `{y}` – год
  - `{mon}` – сокращенное название месяца
  - `{month}` – полное название месяца
  - `'datetime'` – возвращает объект `datetime`
  - `'date'` – возвращает объект `date`
- **`lang`** – язык (`en` или `ru`)
- **`save_history`** – сохранять ли историю сгенерированных дат (по умолчанию `True`)

## Исключения

- `LanguageError` — если передан неподдерживаемый язык.
- `ValueError` — если заданы некорректные диапазоны для дня, месяца или года.

## Лицензия

Проект распространяется под лицензией MIT.

