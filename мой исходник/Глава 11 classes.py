###########  3v2
class Person:
    def __init__(self,name,number):
        self.__name=name
        self.__number=number
    def set_name(self):
        self.__name=name

    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number


class Customer(Person):
    def __init__(self,name,number,id,sent):
        Person.__init__(self,name,number)
        self.__id=id
        self.__sent=sent

    def get_id(self):
        return self.__id
    def get_sent(self):
        return self.__sent


#### 3 v1
class Person:
    def __init__(self,name,number):
        self.__name=name
        self.__number=number
    def set_name(self):
        self.__name=name

    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number


class Customer(Person):
    def __init__(self,name,number,id):
        Person.__init__(self,name,number)
        self.__id=id

    def get_id(self):
        return self.__id

######### 2
class Employer: # надкласс Employer
    def __init__(self,name,id):
        self.__name=name
        self.__id=id

    def set_id(self,id):
        self.__id=id
    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id

    def __str__(self):
        result= self.__name+ ' '+str(self.__id)
        return result

class ShiftSupervisor(Employer):
    def __init__(self,name,id,salary,premium):
        Employer.__init__(self, name, id)
        self.__salary=salary
        self.__premium = premium

    def get_salary(self):  # без методов модификаторов set./////
        return self.__salary
    def get_premium(self):
        return self.__premium

######### 1
class Employer: # надкласс Employer
    def __init__(self,name,id):
        self.__name=name
        self.__id=id

    def set_id(self,id):
        self.__id=id
    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id

    def __str__(self):
        result= self.__name+ ' '+str(self.__id)
        return result

class ProductionWorker(Employer): # подклас ProductionWorker
    def __init__(self,name,id,shift,rate):
        Employer.__init__(self,name,id) #через метод init вызов надкласса Employer и передать аргументы
        self.__shift=shift  # Инициализировать атрибуты shift и rate.
        self.__rate=rate

    def set_shift(self,shift):  # Методы-модификаторы для атрибутов shift и rate.
        self.__shift=shift

    def set_rate(self,rate):
        self.__rate=rate

    def get_rate(self):  # Методы-получатели для атрибутов shift и rate.
        return self.__rate
    def get_shift(self):
        return self.__shift

    def __str__(self):
        result= self.__rate + self.__shift #+self.__name+self.__id
        return result