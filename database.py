# from sqlalchemy import create_engine, text
import pymysql

host="viaduct.proxy.rlwy.net"
username="root"
password="qALgvEGkxBtHopJKJPVPZOmUOIXWoitD"
database = "JovianProject"
port_number = 46747
connection_string = f"mysql+pymysql://{host}:{password}@{host}:{port_number}/{database}?charset=utf8mb4"

connection = pymysql.connect(
    host=host,
    user=username,
    password=password,
    database=database,
    port=port_number
)

# with connection.cursor() as cursor:
#   sql = "SELECT * FROM JovianProject.JobPosting"
#   cursor.execute(sql)

#   results = cursor.fetchall()
#   # column_values = [row for row in results]
#   column_names = [desc[0] for desc in cursor.description]
#   dict_result = [dict(zip(column_names, row))  for row in results]
  
#   print(dict_result)
  # print(type(results))
  # for row in results:
  #     print(row)
  #     print(type(row))


  
# engine = create_engine(
#   connection_string
# )

# with engine.connect() as conn:
#   result = conn.execute(text("select * from JobPosting"))
#   print(result.all())