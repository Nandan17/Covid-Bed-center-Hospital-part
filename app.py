from flask import Flask, render_template, session, redirect, url_for, session, flash,request
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
from models import db, Contact, Hospital, Bed, Patient, app
from forms import InfoForm





# Configure a secret SECRET_KEY
app.config['SECRET_KEY'] = 'mysecretkey'


'''h = Hospital(name='Father Muller Hospital', area='badyar', district='D.K', state='Karnataka', total_beds=1000, available_beds=900,\
                 total_ward_beds=250, available_ward_beds=225, total_ward_beds_with_oxygen=300,\
                 available_ward_beds_with_oxygen=275, total_icu_beds=350, available_icu_beds=325,\
                 total_icu_beds_with_oxygen=100, available_icu_beds_with_oxygen=75)
db.session.add(h)
db.session.commit()

h1 = Hospital(name='Preetham emergency', area='mattikere', district='Banglore', state='Karnataka', total_beds=3450, available_beds=950,\
                 total_ward_beds=210, available_ward_beds=425, total_ward_beds_with_oxygen=200,\
                 available_ward_beds_with_oxygen=275, total_icu_beds=350, available_icu_beds=325,\
                 total_icu_beds_with_oxygen=140, available_icu_beds_with_oxygen=75)
db.session.add(h1)
db.session.commit()

h2 = Hospital(name='Nandan clinic', area='mattikere', district='Banglore', state='Karnataka', total_beds=300, available_beds=34,\
                 total_ward_beds=210, available_ward_beds=425, total_ward_beds_with_oxygen=200,\
                 available_ward_beds_with_oxygen=275, total_icu_beds=350, available_icu_beds=325,\
                 total_icu_beds_with_oxygen=140, available_icu_beds_with_oxygen=75)
db.session.add(h2)
db.session.commit()

h2 = Hospital(name='Siddarth multispeciality', area='mattikere', district='Banglore', state='Andra', total_beds=800, available_beds=34,\
                 total_ward_beds=210, available_ward_beds=425, total_ward_beds_with_oxygen=200,\
                 available_ward_beds_with_oxygen=275, total_icu_beds=350, available_icu_beds=325,\
                 total_icu_beds_with_oxygen=140, available_icu_beds_with_oxygen=75)
db.session.add(h2)
db.session.commit()



b1 = Bed(bed_number=1, type='ward', cost=10000, hospital=h)
b2 = Bed(bed_number=2, type='ward', cost=10000, hospital=h)
b3 = Bed(bed_number=3, type='ward', cost=10000, hospital=h)
b4 = Bed(bed_number=4, type='ward', cost=10000, hospital=h)
b5 = Bed(bed_number=5, type='ward', cost=10000, hospital=h)
b6 = Bed(bed_number=1, type='ward with oxygen', cost=20000, hospital=h)
b7 = Bed(bed_number=2, type='ward with oxygen', cost=20000, hospital=h)
b8 = Bed(bed_number=3, type='ward with oxygen', cost=20000, hospital=h)
b9 = Bed(bed_number=4, type='ward with oxygen', cost=20000, hospital=h)
b10 = Bed(bed_number=5, type='ward with oxygen', cost=20000, hospital=h)
b11 = Bed(bed_number=1, type='ICU', cost=30000, hospital=h)
b12 = Bed(bed_number=2, type='ICU', cost=30000, hospital=h)
b13 = Bed(bed_number=3, type='ICU', cost=30000, hospital=h)
b14 = Bed(bed_number=4, type='ICU', cost=30000, hospital=h)
b15 = Bed(bed_number=5, type='ICU', cost=30000, hospital=h)
b16 = Bed(bed_number=1, type='ICU with oxygen', cost=40000, hospital=h)
b17 = Bed(bed_number=2, type='ICU with oxygen', cost=40000, hospital=h)
b18 = Bed(bed_number=3, type='ICU with oxygen', cost=40000, hospital=h)
b19 = Bed(bed_number=4, type='ICU with oxygen', cost=40000, hospital=h)
b20 = Bed(bed_number=5, type='ICU with oxygen', cost=40000, hospital=h)
db.session.add(b1)
db.session.add(b2)
db.session.add(b3)
db.session.add(b4)
db.session.add(b5)
db.session.add(b6)
db.session.add(b7)
db.session.add(b8)
db.session.add(b9)
db.session.add(b10)
db.session.add(b11)
db.session.add(b12)
db.session.add(b13)
db.session.add(b14)
db.session.add(b15)
db.session.add(b16)
db.session.add(b17)
db.session.add(b18)
db.session.add(b19)
db.session.add(b20)
db.session.commit()'''


@app.route('/', methods=['GET','POST'])
def index():
    name=False
    district=False
    state=False
    area=False
    beds= False
    form = InfoForm() 
    page = request.args.get('page', 1, type=int)
    print('page: ', page)
    
    if request.method == 'POST':
        name = form.name.data
        district = form.district.data
        state = form.state.data
        area = form.area.data
        beds = form.beds.data
        page = 1
        print(name)
        print(district)
    
    if request.method == 'GET':
        name = request.args.get('name')
        state = request.args.get('state')
        district = request.args.get('district')
        area = request.args.get('area')
        beds = request.args.get('beds')
    # data = Hospital.query.order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page) 
    if form.validate_on_submit() and request.method == "POST":
        print('POST request')
        
        
        #print(request.form['name'])
        # print(form.name.data)
        
    data = Hospital.query.order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
    # if request.method == "POST":
        
        #print(request.form['name'])
        # if name =='Please Select':
        #     name_avail = False
        # if district =='Please Select':
        #     district_avail = False
        # if state =='Please Select':
        #     state_avail = False
        # if area =='Please Select':
        #     area_avail = False
        
    if(name =='Please Select' and district =='Please Select' and state =='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)        
        elif beds== 'available_beds':
            data = Hospital.query.order_by(Hospital.available_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name !=  'Please Select' and district =='Please Select' and state =='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name ==  'Please Select' and district !='Please Select' and state =='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(district=district).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(district=district).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(district=district).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(district=district).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name ==  'Please Select' and district =='Please Select' and state !='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(state=state).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(state=state).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(state=state).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(state=state).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(state=state).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(state=state).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
    
    elif(name ==  'Please Select' and district =='Please Select' and state =='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
    
    elif(name !=  'Please Select' and district !='Please Select' and state =='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, district=district).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, district=district).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, district=district).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, district=district).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name !=  'Please Select' and district =='Please Select' and state !='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, state=state).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, state=state).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, state=state).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, state=state).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, state=state).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, state=state).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name !=  'Please Select' and district =='Please Select' and state =='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name ==  'Please Select' and district !='Please Select' and state !='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(district=district, state=state).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(district=district, state=state).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(district=district, state=state).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district, state=state).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(district=district, state=state).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district, state=state).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name ==  'Please Select' and district !='Please Select' and state =='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(district=district, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(district=district, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(district=district, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(district=district, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name ==  'Please Select' and district =='Please Select' and state !='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(state=state, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(state=state, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(state=state, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(state=state, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(state=state, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(state=state, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)


    elif(name !=  'Please Select' and district !='Please Select' and state !='Please Select' and area =='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district, state=state).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district, state=state).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name !=  'Please Select' and district !='Please Select' and state =='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, district=district, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, district=district, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, district=district, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, district=district, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)


    elif(name !=  'Please Select' and district =='Please Select' and state !='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, state=state, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, state=state, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, state=state, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, state=state, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, state=state, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, state=state, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name ==  'Please Select' and district !='Please Select' and state !='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(district=district, state=state, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(district=district, state=state, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(district=district, state=state, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district, state=state, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(district=district, state=state, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(district=district, state=state, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    elif(name !=  'Please Select' and district !='Please Select' and state !='Please Select' and area !='Please Select'):
        if beds == 'total_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state, area=area).order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        elif beds== 'available_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state, area=area).order_by(Hospital.available_beds).paginate(per_page=5, page=page)
        elif beds == 'available_ward_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state, area=area).order_by(Hospital.available_ward_beds.desc()).paginate(per_page=5, page=page)        
        elif beds == 'available_ward_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district, state=state, area=area).order_by(Hospital.available_ward_beds_with_oxygen.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds':
            data = Hospital.query.filter_by(name=name, district=district, state=state, area=area).order_by(Hospital.available_icu_beds.desc()).paginate(per_page=5, page=page)
        elif beds == 'available_icu_beds_with_oxygen':
            data = Hospital.query.filter_by(name=name, district=district, state=state, area=area).order_by(Hospital.available_icu_beds_with_oxygen.desc()).paginate(per_page=5, page=page)

    else:
        data = Hospital.query.order_by(Hospital.total_beds.desc()).paginate(per_page=5, page=page)
        print("Get Request")
    form.name.data = name
    form.district.data = district
    form.state.data = state
    form.area.data = area
    form.beds.data = beds
    return render_template('index.html', form=form, name=name, district=district, state=state, area=area, beds=beds, hospitals=data)




if __name__ == '__main__':
    app.run(debug=True)