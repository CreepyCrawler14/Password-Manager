from flask import Flask, render_template, request
import sys
import random
import string

app = Flask(__name__)

def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    length = random.randint(8, 12)

    all_chars = letters + digits + special_chars

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def store_password(password_name, password):
    try:
        with open('my_passwords.txt', 'a') as file:
            file.write(f'{password_name}: {password}\n')
            print(f'Password stored in my_passwords.txt')
    except FileNotFoundError:
        with open('stored_passwords.txt', 'w') as file:
            file.write(f'{password_name}: {password}\n')
            print(f'Password stored in stored_passwords.txt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password/<password_name>')
def generate_and_store_password(password_name):
    password = generate_password()
    store_password(password_name, password)
    return f'{password_name}: {password}'

if __name__ == '__main__':
    app.run(debug=True)
