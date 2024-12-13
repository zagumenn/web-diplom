from src.Models.Role import Roles

class RoleController:
    # метод добавления роли
    @ classmethod
    def add(cls, new_name_role):
        Roles.create(name = new_name_role)

    @classmethod
    def get(cls):
        return Roles.select().order_by(Roles.name)

if __name__ == "__main__":

    for row in RoleController.get():
        print(row.name)
    print("--------------------")
    RoleController.add('админ')
    for row in RoleController.get():
        print(row.name)
