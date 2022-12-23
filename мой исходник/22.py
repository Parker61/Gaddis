class Pet:
    def __init__(self,name,type,age):
        self.__name=name #нижнее подчеркивание для сокрытия атрибутов
        self.__type=type
        self.__age=age

    #def set_name(self,name):
        #self.__name=name
    def set_type(self,type):
        self.__type=type
    def set_age(self,age):
        self.__age=age

    def get_name(self):
        return self.__name
    def get_type(self):
        return self.__type
    def get_age(self):
        return self.__age