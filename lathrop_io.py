# all the imports
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash

from contextlib import closing


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = 'mYS3cretKey'

@app.route('/')
def homepage():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()



