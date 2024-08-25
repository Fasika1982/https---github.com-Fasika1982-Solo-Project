from flask_app import app
from flask import render_template, request, redirect, session, flash # type: ignore
from flask_app.models.user import User
from flask_app.models.report import Report



@app.route('/report/dashboard')
def report_dashboard():
    if session['user_id']:
        this_user = User.get_by_id(session['user_id'])
        session['user_name'] = f"{this_user.first_name} {this_user.last_name}"       
        return render_template('dashboard.html', reports = Report.get_all())
    return redirect('/')

@app.route('/report/new')
def report_new():
    if session['user_id']:
        
        return render_template('create.html')
    return redirect('/')

@app.route('/report/create', methods=['POST'])
def report_create():
    if session['user_id']:
        print(request.form)
        if Report.valid(request.form):
            print("That's Valid")
            Report.save(request.form)
            return redirect('/report/dashboard')
        return redirect('/report/new') 
    return redirect('/')


@app.route('/report/edit/<int:report_id>')
def report_edit(report_id):
    print(request.form)
    if session['user_id']:       
        this_report = Report.get_by_id(report_id)
        if 'form_input' not in session:
            print(this_report)
            print(this_report.id)
            session['form_input'] = {
                'project_name' : this_report.project_name,
                'job_no' : this_report.job_no,
                'date' : this_report.date,
                'report' : this_report.report,            
            }   
        return render_template('/edit_report.html', report = this_report)
    return redirect('/')  

@app.route('/report/update/<int:report_id>', methods=['POST'])
def report_update(report_id):
    if session['user_id']:
        print(request.form)
        session['form_input'] = request.form.to_dict()
        print(session)
        if Report.edit_valid(request.form):
            print("That's Valid")
            Report.update_by_id(request.form, report_id)
            session.pop('form_input', None)
            return redirect(f'/report/dashboard')
        print("That's In Valid")
        return redirect(f'/report/edit/{report_id}')
    return redirect('/') 

@app.route('/report/delete/<int:report_id>')
def delete_one(report_id):
    Report.delete_one({'id' : report_id})
    return redirect('/report/dashboard')

@app.route('/report/view/<int:report_id>')
def view_one(report_id):
    print(request.form)
    if session['user_id']:
        this_report = Report.get_by_id(report_id)
       
        return render_template('/View.html', report = this_report )
    return redirect('/')  

@app.route('/report/view/<int:report_id>')
def view(report_id):
    print(request.form)
    if session['user_id']:
        this_report = Report.get_by_id(report_id)
       
        return render_template('/View.html', report = this_report )
    return redirect('/') 
        
  






