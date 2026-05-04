from flask import Flask

training = Flask(__name__)

@training.route('/')
def index():
    return 'Training Chat is loading'

if __name__ == '__main__':
    training.run()