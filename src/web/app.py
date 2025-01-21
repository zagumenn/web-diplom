from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, current_user, login_user, login_required, logout_user

from src.Controllers.OrderController import OrderController
from src.Controllers.RoleController import RoleController
from src.Controllers.UserController import UserController
from src.Controllers.CarController import CarController
from src.Models.User import Users




app = Flask(__name__)
app.config['SECRET_KEY'] = 'ваш_секретный_ключ'  # Установите уникальный и секретный ключ
login_manager = LoginManager(app)

# Создание маршрута
@login_manager.user_loader
def load_user(id):
    return Users.get_or_none(int(id))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        print('логин = ', login)
        print('пароль = ', password)
        if UserController.auth(login, password):
            user = UserController.show_login(login)
            login_user(user)
            print(current_user.fullname)
            if user.role_id.name == 'Админ':
                return redirect('/admin')
            elif user.role_id.name == 'Пользователь':
                return redirect('/user')
            else:
                message = f'Извините {login}, но такой роли не существует'
        else:
            message = 'Неверный логин или пароль'
    return render_template('login.html', message=message)

@app.route('/roles')
def roles():
    roles = RoleController.get()
    return render_template('admin.html')

@app.route('/admin')
@login_required  # Убедитесь, что только администраторы или авторизованные пользователи могут видеть эту страницу
def admin():
    users = UserController.get_non_admin_users()
    orders = OrderController.get()
    cars = CarController.get()
    return render_template('admin.html', users=users, orders = orders, cars = cars)

@app.route('/user')
@login_required
def user():
    if current_user.role_id.name == 'Админ':
        users = UserController.get()
        return render_template('admin.html', users=users)
    else:
        return render_template('user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()  # Используем logout_user для завершения сессии
    return redirect('/')  # Перенаправляем на главную страницу


# @app.route('/registration/', methods=['GET', 'POST'])
# def registration():
#     if request.method == 'POST':
#         fullname = request.form['fullname']
#         gender_id = request.form['gender']
#         login = request.form['login']
#         phone = request.form['phone']
#         password = request.form['password']
#
#         role_id = 2  # Например, 2 - стандартная роль пользователя
#
#         # Попытка зарегистрировать пользователя
#         result = UserController.registration(fullname, gender_id, phone, login, password)
#
#         if isinstance(result, str):  # Если это строка, значит, это сообщение об ошибке
#             flash(result)  # Отображаем ошибку
#             return redirect(url_for('registration'))
#         else:
#             flash("Регистрация прошла успешно!")
#             return redirect(url_for('home'))
#
#     return render_template('registration.html')

@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        fullname = request.form['fullname']
        gender = request.form['gender']  # Получаем одно значение

        # Проверяем, какой пол выбран
        if gender == 'male':
            gender_id = 'Мужской'
        elif gender == 'female':
            gender_id = 'Женский'
        else:
            # Если ни один не выбран, можно обработать ошибку
            flash('Пожалуйста, выберите пол', 'error')
            return redirect('/registration/')

        login = request.form['login']
        phone = f"+7{request.form['phone1']}{request.form['phone2']}{request.form['phone3']}"
        password = request.form['password']

        role_id = 2  # Например, 2 - стандартная роль пользователя

        # Попытка зарегистрировать пользователя
        result = UserController.registration(fullname, gender_id, phone, login, password)

        # Обработка успешной регистрации (например, редирект на главную страницу)
        if result:
            flash('Регистрация прошла успешно!', 'success')
            return redirect('/')

        # Обработка ошибок
        flash('Ошибка регистрации', 'error')
        return redirect('/registration/')

    # Если метод запроса GET, возвращаем страницу регистрации
    return render_template('registration.html')  # Убедитесь, что у вас есть шаблон registration.html



@app.route('/orderCreate/')
def orderCreate():
    return render_template('orderCreate.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

