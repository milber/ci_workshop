import os

from flask import Flask

app = Flask(__name__)


@app.route('/quemasve')
def national_statistic():

    return "aquifff"


if __name__ == '__main__':
    port = os.environ["PORT"]
    print('using port : ', port)
    app.run(port=port, host='0.0.0.0')
