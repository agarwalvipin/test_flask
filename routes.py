from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, FloatField, SelectField
from wtforms.fields.html5 import DateField
#from wtforms import *
from wtforms.validators import Required, Length, NumberRange
#from wtforms.validators import *
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET KEY!!'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:60135@localhost/expenses'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vipin:60135@localhost/expenses'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ygrplbehjbnwql:3LkE8j7RkmPUihq6aV2IE7eWbI@ec2-54-225-192-128.compute-1.amazonaws.com:5432/d3cu4huiao9qrr'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'vipin339.mysql.pythonanywhere-services.com'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class ExpenseForm(Form):
    amt         = FloatField('Amount',validators=[Required(),NumberRange(min=0.0, max=999999)])
    date        = DateField('Date', validators=[Required()])
    description = StringField('Description', validators=[Length(0,64)	])
    comments    = StringField('Comment', validators=[Length(0,128)	])
    category    = SelectField(u'Category', choices=[
                                                    ('HOH', 'House hold'),
                                                    ('RAT', 'Ration'),
                                                    ('VGF', 'Veggies & fruits'),
                                                    ('CC', 'Child Care'),
                                                    ('MSC', 'Misc'),
                                                    ('MOB', 'Mobile'),
                                                    ('BCH', 'Bank Charges'),
                                                    ('INT', 'Internet'),
                                                    ('TV', 'Tv'),
                                                    ('RST', 'Restaurant'),
                                                    ('CLT', 'Clothing'),
                                                    ('TVL', 'Travel & Outing'),
                                                    ('PTL', 'Petrol'),
                                                    ('MS', 'Maid & Servant'),
                                                    ('CSR', 'Car Service & Repair'),
                                                    ('MLK', 'Milk'),
                                                    ('PCA', 'Personal Care'),
                                                    ('OFF', 'Official'),
                                                    ('INC', 'Income')])
    submit = SubmitField('Submit')

class tbl_entry(db.Model):
    __tablename__ = 'tbl_entry'
    id = db.Column(db.Integer, primary_key=True)
    #id = db.column(db.Integer)
    amt = db.Column(db.Float)
    date = db.Column(db.Date) 
    #description = db.column(db.String, length = 64)
    description = db.Column(db.String(64))
    category = db.Column(db.String(64))
    
    
class NameForm(Form):
	name = StringField('Name?', validators=[Required(),Length(1,12)	])
	submit = SubmitField('Submit')

@app.route('/expense', methods = ['GET','POST'])
def expense():
    description = None
    form = ExpenseForm()
    if form.validate_on_submit():
        amt = form.amt.data
        date = form.date.data
        description = form.description.data
        category = form.category.data
        form.amt.data = 0.0
        form.description.data = ''
        form.comments.data = ''
        db.session.add(tbl_entry(amt = amt,date = date, description = description, category = category))
        db.session.commit()
    return render_template('expense.html',form=form, description=description)
    #return render_template('wtflogin.html',form=form)


@app.route('/wtflogin', methods = ['GET','POST'])
def wtflogin():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('wtflogin.html',form=form, name=name)

@app.route('/login', methods = ['GET','POST'])
def login():
	name = None
	if request.method == 'POST' and 'name' in request.form:
		name = request.form['name']
	return render_template('login.html',name = name)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

@app.route('/calendar')
def cal():
	months = [
			'January', 
			'Feburary', 
			'March', 
			'April', 
			'May', 
			'June', 
			'July', 
			'August', 
			'September', 
			'October', 
			'November', 
			'Decmeber', 
		]

	weather = {	'January' : {'min':10,'max':20,'rainfall':30}, 
			'Feburary' : {'min':20,'max':60,'rainfall':40}, 
			'March' : {'min':40,'max':70,'rainfall':50}, 
			'April' : {'min':70,'max':90,'rainfall':60}, 
			'May' 	: {'min':20,'max':40,'rainfall':70}, 
			'June' 	: {'min':23,'max':80,'rainfall':80}, 
			'July' 	: {'min':56,'max':90,'rainfall':90}, 
			'August' : {'min':48,'max':80,'rainfall':100}, 
			'September' : {'min':22,'max':50,'rainfall':10}, 
			'October' : {'min':56,'max':60,'rainfall':20}, 
			'November' : {'min':12,'max':40,'rainfall':30}, 
			'Decmeber' : {'min':11,'max':30,'rainfall':40}, 
		}

	return render_template('calendar.html', city = 'Mumbai', months= months, weather=weather)

if __name__ =='__main__':
	app.run(debug=True)
