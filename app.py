from flask import Flask, render_template, jsonify, request, redirect, url_for, session
app = Flask(__name__)

positions = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': '$80,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': '$100,000'
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Kolkata, India',
        'salary': '$80,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Pune, India',
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=positions, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(positions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# print('name')