from functions.database import connection
def load_jobs_from_db():
  with connection.cursor() as cursor:
      sql = "SELECT * FROM JovianProject.JobPosting"
      cursor.execute(sql)
      results = cursor.fetchall()
      # column_values = [row for row in results]
      column_names = [desc[0] for desc in cursor.description]
      jobs = [dict(zip(column_names, row)) for row in results]
      return jobs


def load_job_from_db(id):
  with connection.cursor() as cursor:
    sql = f"SELECT * FROM JovianProject.JobPosting where id={id}"
    cursor.execute(sql)
    results = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    job = [dict(zip(column_names, row)) for row in results]
    return job


def app_submitted(job_id, data):
  full_name = data['full_name']
  email = data['email']
  linkedin_url = data['linkedin_url']
  education = data['Education']
  work_experience = data['Exp']
  resume = data['Resume']
  jobid = job_id

  sql = """
  INSERT INTO applications 
  (jobid, full_name, email, linkedin_url, education, work_experience, resume_url) 
  VALUES (%s, %s, %s, %s, %s, %s, %s)
  """

  with connection.cursor() as cursor:
      cursor.execute(sql, (jobid, full_name, email, linkedin_url, education, work_experience, resume))
  connection.commit()

def last_submiited_job():
  with connection.cursor() as cursor:
    sql = """
    Select * From applications
    Order by id desc
    Limit 1
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    last_submision = [dict(zip(column_names, row)) for row in results]
    return last_submision

def dropdown1():
  with connection.cursor() as cursor:
    sql = """
    Select id, title From JobPosting
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    val = [dict(zip(column_names, row)) for row in results]
    return val

def get_application_by_jobid(jobid):
  with connection.cursor() as cursor:
    sql = """
    Select CONCAT(ap.id, ' || ', ap.full_name) Application, ap.id, jp.title
    From JovianProject.JobPosting jp
    Inner Join JovianProject.applications ap on jp.id=ap.jobid
    Where jobid=%s
    """
    cursor.execute(sql, (jobid))
    results = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    val = [dict(zip(column_names, row)) for row in results]
    return val

def get_application_status(applid):
  with connection.cursor() as cursor:
    sql = """
    Select statusid, `status`
    from JovianProject.applicationstatus
    where applicationid=%s
    """
    cursor.execute(sql, (applid))
    results = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    val = [dict(zip(column_names, row)) for row in results]
    return val