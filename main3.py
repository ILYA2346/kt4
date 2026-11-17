class User:
    count = 0

    def __init__(self, name, login, password, grade):
        self.name = name
        self.__login = login
        self.__password = password
        self.__grade = grade
        self.__class__.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        print("Невозможно изменить логин!")

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def grade(self):
        return "Неизвестное свойство grade"

    @grade.setter
    def grade(self, value):
        print("Неизвестное свойство grade")

    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}")

    def __eq__(self, other):
        return self.__grade == other.__grade

    def __lt__(self, other):
        return self.__grade < other.__grade

    def __gt__(self, other):
        return self.__grade > other.__grade


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role, grade):
        super().__init__(name, login, password, grade)
        self.role = role

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}, Role: {self.role}")


user1 = User('Paul McCartney', 'paul', '1234', 3)
user2 = User('George Harrison', 'george', '5678', 2)
user3 = User('Richard Starkey', 'ringo', '8523', 3)
admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

user1.show_info()
admin.show_info()

users = User.count
admins = SuperUser.count
print(f'Всего обычных пользователей: {users}')
print(f'Всего супер-пользователей: {admins}')

print(user1 < user2)
print(admin > user3)
print(user1 == user3)

user3.name = 'Ringo Starr'
user1.password = 'Pa$$w0rd'

print(user3.name)
print(user2.password)
print(user2.login)

user2.login = 'geo'

print(user1.grade)
admin.grade = 10
