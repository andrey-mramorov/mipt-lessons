class Animal:
    __age = ''
    __name = ''

    def __init__(self):
        pass

    def set_age(self, age):
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    
class Zebra(Animal):
    __info = ''

    def set_info(self, info):
        self.__info = info
    
    def ger_info(self):
        return self.__info


class Dolphin(Animal):
    __info = ''

    def set_info(self, info):
        self.__info = info
    
    def get_info(self):
        return self.__info
