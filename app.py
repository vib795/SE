from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import subprocess
import shlex

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some?bamboozle#string-foobar'

class NameForm(FlaskForm):
    command = StringField('Type in your search below', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', "POST"])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    form = NameForm()
    message=""
    if request.method == "POST":
        command = form['command'].data
        command = shlex.split(command)
        process = subprocess.Popen(command, stdout = subprocess.PIPE)
        print("Run successfully")
        output, err = process.communicate()
        print(output)
        message="HOLD ON"
        flash(message)
    return render_template('index.html', form=form, message=message)

if __name__ == "__main__": 
    app.run(debug=True)