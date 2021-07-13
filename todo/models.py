from django.db import models


class Employee(models.Model):
    emp_code = models.CharField(max_length=10, unique=True, help_text='emp code ex. LTPL - 4 digit')
    emp_name = models.CharField(max_length=40)
    salary = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.emp_code


class EmpDepartment(models.Model):
    dept_code = models.CharField(max_length=10)
    emp_code = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    dept_name = models.CharField(max_length=30)
