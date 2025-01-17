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


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        fullname = request.form['fullname']
        login = request.form['login']
        password = request.form['password']
        role_id = 2  # Например, 2 - стандартная роль пользователя

        # Попытка зарегистрировать пользователя
        result = UserController.registration(fullname, login, password, role_id)

        if isinstance(result, str):  # Если это строка, значит, это сообщение об ошибке
            flash(result)  # Отображаем ошибку
            return redirect(url_for('registration'))
        else:
            flash("Регистрация прошла успешно!")
            return redirect(url_for('home'))

    return render_template('registration.html')

@app.route('/orderCreate/')
def orderCreate():
    return render_template('orderCreate.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

