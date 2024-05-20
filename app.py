from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from functions.function import load_jobs_from_db, load_job_from_db
app = Flask(__name__)


@app.route('/')
def hello_world():
    joblist= load_jobs_from_db()
    return render_template('home.html', jobs=joblist, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
    joblist= load_jobs_from_db()
    return jsonify(joblist)

@app.route('/job/<id>')
def show_job(id):
    joblist = load_job_from_db(id)
    return render_template('jobpage.html', job=joblist[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# print('name')
# Buy a domain name from domain.google.com to create your own domain. Tutorial starts at 1:38 in the video.
