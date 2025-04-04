import random
import calendar

from datetime import datetime
from datetime import date


class LanguageError(Exception):
    """
    Exception raised when an unsupported language is used.
    """


class GeneratorDates:
    """
    A random date generator with customizable format and language.
    
    Attributes:
        format (str): Date output format supporting the following parameters:
            - {d}: Day of the month.
            - {m}: Numeric representation of the month.
            - {y}: Year.
            - {mon}: Short month name (based on selected language).
            - {month}: Full month name (based on selected language).
            - 'datetime': Returns a datetime object.
            - 'date': Returns a date object.
        lang (str): Output language ('en' or 'ru').
        save_history (bool): Whether to save generated dates in history.
        history (list): Stores generated dates if save_history is enabled.
    """

    months = {
        "en": {
            "full": {
                1: "january",
                2: "february",
                3: "march",
                4: "april",
                5: "may",
                6: "june",
                7: "july",
                8: "august",
                9: "september",
                10: "october",
                11: "november",
                12: "december"
            },
            "short": {
                1: "jan",
                2: "feb",
                3: "mar",
                4: "apr",
                5: "may",
                6: "jun",
                7: "jul",
                8: "aug",
                9: "sep",
                10: "oct",
                11: "nov",
                12: "dec"
            }
        },

        "ru": {
            "full": {
                1: "января",
                2: "февраля",
                3: "марта",
                4: "апреля",
                5: "мая",
                6: "июня",
                7: "июля",
                8: "августа",
                9: "сентября",
                10: "октября",
                11: "ноября",
                12: "декабря"
            },
            "short": {
                1: "янв",
                2: "фев",
                3: "мар",
                4: "апр",
                5: "мая",
                6: "июн",
                7: "июл",
                8: "авг",
                9: "сен",
                10: "окт",
                11: "ноя",
                12: "дек"
            }
        }
    }


    def __init__(self, format='{d} {mon} {y}', lang='en', save_history=True):
        """
        Initializes the date generator with a specified format and language.
    
        Parameters:
            format (str): Defines how the generated date is presented. Supports:
                - {d}: Day of the month.
                - {m}: Numeric representation of the month.
                - {y}: Year.
                - {mon}: Short month name (based on selected language).
                - {month}: Full month name (based on selected language).
                - 'datetime': Returns a datetime object.
                - 'date': Returns a date object.
            lang (str): Language of the output ('en' for English, 'ru' for Russian).
            save_history (bool): Whether to store generated dates in history (default True).
    
        Raises:
            LanguageError: If an unsupported language is provided.
        """

        self.format = format
        if lang not in ['en', 'ru']:
            raise LanguageError(f'Unsupported language: {lang}')
        self.lang = lang
        
        self.history = []
        self.save_history = save_history
    
    def generate_date(self, range_day=(1, 28), range_month=(1, 12), range_year=(1950, 2000)):
        """
        Generates a random date within the given ranges.
        
        Parameters:
            range_day (tuple): Range for the day (default (1, 28)).
            range_month (tuple): Range for the month (default (1, 12)).
            range_year (tuple): Range for the year (default (1950, 2000)).
        
        Returns:
            str | datetime | date: Randomly generated date in the specified format.
        
        Raises:
            ValueError: If the provided ranges are invalid.
        """
        
        if not isinstance(range_day, tuple) or len(range_day) != 2:
            raise ValueError(f'Incorrect range day: {range_day}')
        if not isinstance(range_month, tuple) or len(range_month) != 2:
            raise ValueError(f'Incorrect range month: {range_month}')
        if not isinstance(range_year, tuple) or len(range_year) != 2:
            raise ValueError(f'Incorrect range year: {range_year}')

        if range_year[0] <= 0:
            range_year = (1, range_year[-1])
        if range_year[-1] <= 0:
            range_year = (range_year[0], 1)
        year = random.randint(*range_year)

        max_month = 12
        if range_month[0] > max_month:
            range_month = (max_month, range_month[-1])
        if range_month[0] <= 0:
            range_month = (0, range_month[-1])
        if range_month[-1] > max_month:
            range_month = (range_month[0], max_month)
        if range_month[-1] <= 0:
            range_month = (range_month[0], 1)
        month = random.randint(*range_month)

        max_day = calendar.monthrange(year, month)[1]
        if month == 2 and year % 4 != 0:
            max_day = 28
        if range_day[0] > max_day:
            range_day = (max_day, range_day[-1])
        if range_day[0] <= 0:
            range_day = (1, range_day[-1])
        if range_day[-1] > max_day:
            range_day = (range_day[0], max_day)
        if range_day[-1] <= 0:
            range_day = (range_day[0], 1)
        day = random.randint(*range_day)
        
        if self.format == 'datetime':
            random_date = datetime(year, month, day)
        elif self.format == 'date':
            random_date = date(year, month, day)
        else:
            random_date = self.format.format(
                d=day, m=month, y=year,
                mon=self.months[self.lang]['short'][month],
                month=self.months[self.lang]['full'][month]
            )
        
        if self.save_history:
            self.history.append(random_date)
        return random_date



def check_class():
    """
    Runs a test to generate and print random dates using different formats.
    
    The function initializes two GeneratorDates instances:
    1. One with the default format ('{d} {mon} {y}') and prints 3 random dates.
    2. Another with the 'datetime' format and prints 3 random datetime objects.
    
    Additionally, it prints the history of generated dates for both instances.
    """

    generator = GeneratorDates()
    for i in range(1, 4):
        random_date = generator.generate_date()
        print(f'{i} random date: {random_date}')
    print(generator.history, end='\n\n')
    
    generator = GeneratorDates(format='datetime')
    for i in range(1, 4):
        random_date = generator.generate_date()
        print(f'{i} random date datetime: {random_date}')
    print(generator.history)


if __name__ == '__main__':
    check_class()