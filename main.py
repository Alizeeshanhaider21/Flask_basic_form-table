from flask import Flask, render_template,redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired
import csv



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    Location = StringField('Location', validators=[DataRequired()])
    opening_time = StringField('Opening Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    rating = SelectField('Rating', choices=['✘','☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️'],validators=[DataRequired()]) 
    wifi_rating = SelectField('Wifi Rating', choices=['✘','💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪'],validators=[DataRequired()]) 
    power_outlet = SelectField('Power Outlet', choices=['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌'],validators=[DataRequired()]) 
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        cafe = form.cafe.data 
        Location = form.Location.data 
        opening_time = form.opening_time.data 
        closing_time = form.closing_time.data 
        rating = form.rating.data 
        wifi_rating = form.wifi_rating.data 
        power_outlet = form.power_outlet.data 
        print(cafe,rating)
        with open('cafe-data.csv', 'a',encoding="utf-8") as f:
            # f.write(f'\n{cafe},'f'{Location},'f'{opening_time},'f'{closing_time},'f'{rating},'f'{wifi_rating},'f'{power_outlet}')
            f.write(f'\n{cafe},{Location},{opening_time},{closing_time},{rating},{wifi_rating},{power_outlet}')
        return redirect(('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
      
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
