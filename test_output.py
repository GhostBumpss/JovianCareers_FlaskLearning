from functions.function import load_job_from_db, last_submiited_job, dropdown1, get_application_status

# output = load_job_from_db(2)
# print(output[0]['responsibilities'].split(', '))

# last_application = last_submiited_job()
# print(last_application)

# dropdown1 = dropdown1()
# print(dropdown1)

appstatus = get_application_status(13)
print(appstatus)