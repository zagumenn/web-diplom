from src.Models.User import *
from bcrypt import hashpw, gensalt, checkpw


class UserController:
    @classmethod
    def get(cls):
        return Users.select()

    @classmethod
    def registration(cls, fullname, login, password, role_id):
        # Проверка логина
        if Users.select().where(Users.login == login):
            return "Пользователь с таким логином существует, попробуйте снова"

        # Хеширование пароля
        hash_password = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
        Users.create(fullname=fullname, login=login, password=hash_password, role_id=role_id)
        return f"Пользователь {login} добавлен в систему"

    @classmethod
    def auth(cls, login, password):

        if Users.get_or_none(Users.login == login) != None:
            hash_password = Users.get_or_none(Users.login == login).password

            if checkpw(password.encode('utf-8'), hash_password.encode('utf-8')):
                return True

        return False

    @classmethod
    def show(cls, id):
        return Users.get_or_none(id)

    @ classmethod
    def delete(cls, id):
        Users.delete_by_id(id)

    @classmethod
    # Метод, который выводит id по имени
    def show_login(cls, login):
        return Users.get(Users.login == login)

    @classmethod
    def get_non_admin_users(cls):
        # Предполагается, что роль администратора имеет id = 1
        # Измените это значение в зависимости от вашей структуры ролей
        admin_role_id = 1
        return Users.select().where(Users.role_id != admin_role_id)

if __name__ == "__main__":
    #print(UserController.registration('Oleg', 'olg19', 'olg12345', 1))
    print(UserController.auth('ivan89', '111111111'))
    print(UserController.show_login('olg19').role_id)
