from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from functions.function import last_submiited_job, load_jobs_from_db, load_job_from_db, app_submitted
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
    print(new_application)
    # print(joblist[0])
    # return jsonify(data)
    return render_template('Application_submitted.html', application=new_application[0], job=joblist[0])


# @app.route('/job/<id>/apply', methods=['get'])
# def apply_to_job(id):
#     data = request.args
#     return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# print('name')
# Buy a domain name from domain.google.com to create your own domain. Tutorial starts at 1:38 in the video.
