from demo.todo.models import Employee

employee_dict = [
                {
                    "emp_code": "LTPL007",
                    "name": "Bhavin",
                    "sal": 60000
                },
                {
                    "emp_code": "LTPL008",
                    "name": "Gaurav",
                    "sal": 80000
                },
                {
                    "emp_code": "LTPL0009",
                    "name": "Keval",
                    "sal": 40000
                }
]
for emp_data in employee_dict:
    Employee.objects.create(emp_code=emp_data['emp_code'], emp_name=emp_data['name'], salary=emp_data['salary'])
    print(emp_data['name'], emp_data['sal'])

Employee.objects.get_or_create(emp_code="LTPL04", emp_name="Ajay", salary=15000)
Employee.objects.create(emp_code="LTPL04", emp_name="Ajay", salary=15000)
Employee.objects.create(emp_code="LTPL05", emp_name="Raj", salary=10000)
Employee.objects.get(emp_code="LTPL110")
Employee.objects.filter(emp_code="LTPL110", emp_name="Raj")

try:
    Employee.objects.filter(salary__gte=10000, salary__lt=25000)
except Employee.DoesNotExist:
    print("Not found")
except Exception as e:
    print(e)


Employee.objects.get(emp_code="LTPL110")

"select * from employee where emp_code=LTPL110"

