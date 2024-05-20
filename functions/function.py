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