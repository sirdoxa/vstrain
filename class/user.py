from pprint import pprint


class UserList(list['User']):
    def search (self, user_name: str) -> list['User']:
        matching_users: list['User'] = []
        for user in self:
            if user_name in user.user_name:
                matching_users.append(user)
        return matching_users
    

class User(object):
    all_users: list(['user']) = UserList()


    def __init__(self, user_name: str, email: str, password:str):
        self.user_name = user_name
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.user_name!r}, {self.email!r}, '\
        f'{self.password!r})'
    
    def __str__(self):
        return f'{self.user_name}'
    

class Seller(User):
    def order(self, order: 'Order') -> None:
        print(f'{self.user_name}, from your products, {order} was sold!')


def main():
    user1 = User('mahdi','mhdy','364')
    user1 = User('ali','ofh','146')
    user1 = User('taha','jdi','784')
    pprint(User.all_users.search('m'))


if '__main__' == __name__:
    main()