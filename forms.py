from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,validators,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired


# Now create a WTForm Class
class InfoForm(FlaskForm):
    name = SelectField('Name', choices=[('Please Select','Please Select'),('Preetham emergency','Preetham emergency'),('Nandan clinic','Nandan clinic'),('Siddarth multispeciality','Siddarth multispeciality'),('Father Muller Hospital','Father Muller Hospital')])
    district = SelectField('District: ', choices=[('Please Select','Please Select'),('D.K','D.K'),('Banglore','Banglore')])
    state = SelectField('State: ', choices=[('Please Select','Please Select'),('Andra','Andra'),('Karnataka','Karnataka')])
    area = SelectField('Area: ', choices=[('Please Select','Please Select'),('badyar','badyar'),('mattikere','mattikere')])
    beds = RadioField('Sort bed results by ',[validators.Required()], choices=[('total_beds','total_beds'),('available_beds','available_beds'),('available_ward_beds','available_ward_beds'),('available_ward_beds_with_oxygen','available_ward_beds_with_oxygen'),('available_icu_beds','available_icu_beds'),('available_icu_beds_with_oxygen','available_icu_beds_with_oxygen')], default='total_beds')
    submit = SubmitField('Search')