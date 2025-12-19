import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='college',
    database="employees",
    ssl_disabled=True
)
cursor = connection.cursor()
query = """
SELECT * from employees e 
JOIN salaries s on e.emp_no =s.emp_no 
WHERE e.hire_date > '1999-01-01'
"""
cursor.execute(query)
for i,data in enumerate(cursor.fetchall()):
    print(data)