import random

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
        lang (str): Output language ('en' or 'ru').
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


    def __init__(self, format='{d} {mon} {y}', lang='en'):
        """
        Initializes the date generator.
        
        Parameters:
            format (str): Date format (default '{d} {mon} {y}').
            lang (str): Language ('en' or 'ru').
        
        Raises:
            LanguageError: If an unsupported language is provided.
        """

        self.format = format
        if lang not in ['en', 'ru']:
            raise LanguageError(f'Unsupported language: {lang}')
        self.lang = lang
    
    def generate_date(self, range_day=(1, 28), range_month=(1, 12), range_year=(1950, 2000)):
        """
        Generates a random date within the given ranges.
        
        Parameters:
            range_day (tuple): Range for the day (default (1, 28)).
            range_month (tuple): Range for the month (default (1, 12)).
            range_year (tuple): Range for the year (default (1950, 2000)).
        
        Returns:
            str: Randomly generated date in the specified format.
        """

        day = random.randint(*range_day)
        month = random.randint(*range_month)
        year = random.randint(*range_year)
        
        random_date = self.format.format(
            d=day, m=month, y=year,
            mon=self.months[self.lang]['short'][month],
            month=self.months[self.lang]['full'][month]
        )
        return random_date


def check_class():
    """
    Test function to generate and print 10 random dates.
    """

    generator = GeneratorDates()
    for i in range(1, 11):
        random_date = generator.generate_date()
        print(f'{i} random date: {random_date}')



if __name__ == '__main__':
    check_class()