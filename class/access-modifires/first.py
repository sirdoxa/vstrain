# underscore:
# public: name
# private: __name --> name mangling
# protected: _name

class User:
    def __init__(self, name='', phone=''):
        self.userid = id(self)
        self.name = name
        self.__phone = phone
    
    def set_phone(self, phone):
        if len(phone) == 11 and phone.isdigit():
            self.__phone = phone

    def get_phone(self):
        return self.__phone


ali = User()
ali.set_phone('09191231564')
phone_number = ali.get_phone()
print(phone_number)
    