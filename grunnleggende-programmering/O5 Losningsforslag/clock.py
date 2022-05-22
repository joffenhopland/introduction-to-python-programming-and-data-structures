class Clock:
    def __init__(self, day=0, month=0, year=0, hour=0, min=0, sec=0):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__hour = hour
        self.__min = min
        self.__sec = sec

    def inc_sec(self):
        self.__sec += 1
        if self.__sec == 60:
            self.__sec = 0
            self.inc_min()

    def inc_min(self):
        self.__min += 1
        if self.__min == 60:
            self.__min = 0
            self.inc_hour()

    def inc_hour(self):
        self.__hour += 1
        if self.__hour == 24:
            self.__hour = 0
            self.inc_day()

    def inc_day(self):
        self.__day += 1
        if self.__should_change_month(self.__year):
            self.__day = 1
            self.inc_month()

    def inc_month(self):
        self.__month += 1
        if self.__month == 13:
            self.__month = 1
            self.__year += 1

    def __should_change_month(self, year):
        months_31 = [1, 3, 5, 7, 8, 10, 12]
        months_30 = [4, 6, 9, 11]
        if self.__month in months_31 and self.__day == 31:
            return True
        elif self.__month in months_30 and self.__day == 30:
            return True
        elif self.__is_leapyear(year) and self.__day == 28:
            return False
        elif self.__is_leapyear(year) and self.__day == 29:
            return True
        return False

    def __is_leapyear(self, year):
        return False  # not implemented

    def clock_as_string(self):
        return (f'{self.__day:02d}:{self.__month:02d}:{self.__year:04d}:{self.__hour:02d}:{self.__min:02}:{self.__sec:02}')

    def set_clock(self, day, month, year, hour, min, sec):
        self.__day = day
        self.__month = month
        self.__year = year
        self._hour = hour
        self.min = min
        self.sec = sec


def main():
    clock = Clock(30, 1, 2021, 23, 59, 59)
    clock.inc_sec()
    s = clock.clock_as_string()
    print(s)


if __name__ == "__main__":
    main()
