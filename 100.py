from generation import generate_sql_requests

for request in generate_sql_requests():
    print(request)