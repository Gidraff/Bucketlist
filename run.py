import os
from app import app

if __name__ == '__main__':
    app.secret_key = os.environ.get('SECRET_KEY')
    app.run(debug=True)
