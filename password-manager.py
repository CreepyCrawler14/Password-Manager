from flask import Flask, render_template, request, redirect, url_for
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
            return 'Password stored in my_passwords.txt'
    except FileNotFoundError:
        with open('stored_passwords.txt', 'w') as file:
            file.write(f'{password_name}: {password}\n')
            return 'Password stored in stored_passwords.txt'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_and_store_password():
    password_name = request.form['passwordName']
    password = generate_password()
    store_message = store_password(password_name, password)
    return render_template('index.html', generated_password=f'{password_name}: {password}', store_message=store_message)

if __name__ == '__main__':
    app.run(debug=True)
