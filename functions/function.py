from database import connection
def load_jobs_from_db():
  with connection.cursor() as cursor:
      sql = "SELECT * FROM JovianProject.JobPosting"
      cursor.execute(sql)
      results = cursor.fetchall()
      # column_values = [row for row in results]
      column_names = [desc[0] for desc in cursor.description]
      jobs = [dict(zip(column_names, row)) for row in results]
      return jobs