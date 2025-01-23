from src.Models.Car import Cars

class CarController:

    @classmethod
    def get(cls):
        return Cars.select()

    @classmethod
    def add(cls, brand, model, color, state_number):
        Cars.create(brand = brand, model = model, color = color,
                    state_number = state_number)

    @classmethod
    def update_color(cls, new_color, id_car):
        Cars.update({Cars.color: new_color}).where(Cars.id == id_car).execute()

    @classmethod
    def update_number(cls, new_number, id_car):
        Cars.update({Cars.state_number: new_number}).where(Cars.id == id_car).execute()

    @classmethod
    def delete(cls, id):
        Cars.delete_by_id(id)


if __name__ == "__main__":
    print("---------")
    print(CarController.delete(1))