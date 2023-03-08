import re


class Person:
    def __init__(self, info):
        self.info = ','.join(info)
        self.data = {}

    def __re_finditer(self, pattern):
        return re.finditer(pattern, self.info)

    def __re_search(self, pattern):
        return re.search(pattern, self.info)

    def forming_new_data(self):
        pattern_name = r"([А-Я][а-я]+)(\s+|,)?([А-Я][а-я]+)(\s+|,)?([А-Я][а-я]+)?"
        pattern_organization = r"([А-Я]{2,})|(,[А-Я][а-я]+)"
        pattern_position = r",[a-zа-я]+\s+[а-я]+"
        pattern_phone = r"\+?(7|8)\s?\(?(\d{3})\)?\s?(\d{3})-?(\d{2})-?(\d{2})\s?\(?(доб.\s?\d{4})?"
        pattern_email = r"([a-zA-Z]+\.?[a-zA-Z]+)?(\d+)?@[a-z]+.[a-z]{2,3}"
        patterns = [pattern_name, pattern_organization, pattern_position, pattern_phone, pattern_email]
        return map(lambda x: self.__re_search(x) if x != pattern_organization else self.__re_finditer(x), patterns)
