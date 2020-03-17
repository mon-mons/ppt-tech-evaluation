"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
 
from flask import render_template, request, redirect, url_for, flash
from app.forms import WorkerForm
from app.models import Workers
from app import db, app
from werkzeug.utils import secure_filename
import os 

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/addworker', methods = ['GET', 'POST'])
def addworker():
    workerform= WorkerForm()
    if request.method=='POST' and workerform.validate_on_submit():
        firstname=workerform.firstname.data
        lastname=workerform.lastname.data
        address1=workerform.address1.data
        city=workerform.city.data
        country=workerform.country.data
        telephone_no=workerform.telephone_no.data
        role=workerform.role.data
        email=workerform.email.data
        addresslocation=workerform.addresslocation.data
        flash('Worker has been added!', 'success')
        worker=Workers(first_name=firstname,last_name=lastname, address1= address1, city=city, country=country, telephone_no=telephone_no, role=role, email=email, addresslocation=addresslocation)
        db.session.add(worker)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('addworker.html', form=workerform)

@app.route('/workers')
def workers():
    """Render the website's workers page."""
    employees = Workers.query.all()
    return render_template('workers.html', employees=employees)

# @app.route('/profile/<userid>')
# def loaduserprofile(userid):
#     """Render an individual user profile by the specific user's id."""
#     userprofile =UserProfile.query.filter_by(id=int(userid)).first()
#     return render_template('loaduserprofile.html', userprofile=userprofile)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
