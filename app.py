from flask import Flask, render_template, request, redirect, url_for
from authentication import AuthSingleton
from user_login import LoginCommand, LogoutCommand, Invoker
from flask import redirect

app = Flask(__name__)
auth_instance = AuthSingleton()
invoker = Invoker()


@app.route('/')
def home():
    logged_in_user = auth_instance.get_logged_in_user()
    return render_template('index.html', logged_in_user=logged_in_user)

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        auth_instance.create_user(username, password)
        return redirect(url_for('home'))
    return render_template('create_user.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        login_command = LoginCommand(auth_instance, username, password)
        invoker.set_command(login_command)
        invoker.execute_command()
        return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_command = LogoutCommand(auth_instance)
    invoker.set_command(logout_command)
    invoker.execute_command()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
