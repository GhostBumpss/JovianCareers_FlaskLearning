from types import MethodType
from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from functions.function import last_submiited_job, load_jobs_from_db, load_job_from_db, app_submitted, dropdown1, get_application_by_jobid, get_application_status, login_Created
app = Flask(__name__)


@app.route('/')
def show_jobs():
    joblist= load_jobs_from_db()
    # print(joblist)
    return render_template('home.html', jobs=joblist, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
    joblist= load_jobs_from_db()
    return jsonify(joblist)

@app.route('/job/<id>')
def show_job(id):
    joblist = load_job_from_db(id)
    if joblist:
        return render_template('jobpage.html', job=joblist[0], company_name='Jovian')
    else:
        return 'Not Found', 404


@app.route('/job/<id>/apply', methods=['POST'])
def apply_to_job(id):
    data = request.form
    data_dict = dict(data)
    joblist = load_job_from_db(id)
    app_submitted(job_id=id, data=data_dict)
    new_application = last_submiited_job()
    return render_template('Application_submitted.html', application=new_application[0], job=joblist[0])

@app.route('/dynamic_dropdown', methods=['GET'])
def dynamic_dropdown1():
    jobposts = dropdown1()
    return render_template('dynamic_dropdow.html', jobposts=jobposts)

@app.route('/get_applications/<job_id>', methods=['GET'])
def get_applications(job_id):
    applications = get_application_by_jobid(job_id)
    return jsonify(applications)

@app.route('/applicationStatus/<appid>', methods=['GET'])
def applicationStatus(appid):
    application_status = get_application_status(appid)
    return jsonify(application_status)

@app.route('/loginCreation', methods=['GET'])
def loginCreation():
    return render_template('newform.html')

@app.route('/loginsubmit', methods=['POST'])
def loginsubmit():
    data = request.json
    print(data)
    login_Created(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# print('name')
# Buy a domain name from domain.google.com to create your own domain. Tutorial starts at 1:38 in the video.
# {'user_name': 'basu.majum', 'password': 'S12345', 'email': 'saikatbmd9836@gmail.com', 'phoneno': '9674021332'}