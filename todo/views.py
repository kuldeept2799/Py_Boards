from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm


def dashboard(request):
    emp_obj = Employee.objects.all()
    return render(request, 'dashboard.html', {'emp_obj': emp_obj})


def create_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee successfully created!")
            return redirect('home')
    return render(request, 'create-employee.html', {'form': form})


def edit_employee(request, id):
    if Employee.objects.filter(id=id).exists():
        emp_obj = Employee.objects.get(id=id)
        form = EmployeeForm(instance=emp_obj)
        if request.method == 'POST':
            form = EmployeeForm(request.POST, instance=emp_obj)
            if form.is_valid():
                form.save()
                messages.success(request, "Employee successfully created!")
                return redirect('home')
    else:
        messages.error(request, "Employee with entered id is not exists!")
    return render(request, 'create-employee.html', {'form': form})


def del_employee(request, id):
    check_emp = Employee.objects.filter(id=id)
    if check_emp.exists():
        check_emp.delete()
    messages.success(request, "Employee successfully deleted!")
    return redirect('home')
