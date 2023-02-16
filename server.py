from flask import render_template, request
from config import app

mailing_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration', methods=['POST'])
def registrate():
    email = request.form.get('email')
    mailing_list.append(email)
    return f'your email ({email}) is in our mailing list FOREVER EVER'

@app.route('/am_i_in_the_mailing_list/<email>')
def check_email(email):
    if email in mailing_list:
        return "yes, you are in our mailing list"
    else:
        return 'not yeat'

if __name__ == '__main__':
    app.run()