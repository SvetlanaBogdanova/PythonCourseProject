class Date:
    month_length = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, date):
        self.date = date

    def __str__(self):
        return self.date

    @classmethod
    def checked_date(cls, date):
        try:
            day, month, year = map(int, date.split('-'))
            if not cls.validate(day, month, year):
                print('Неверный формат даты')
            else:
                return cls(date)
        except ValueError:
            print('Неверный формат даты')

    @staticmethod
    def validate(day, month, year):
        return 1 <= month <= 12 and 1 <= day <= Date.month_length[month] and year <= 2030


my_date = Date.checked_date('21-07-2021')
print(my_date)
