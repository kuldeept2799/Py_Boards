import re

from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('emp_code', 'emp_name', 'salary')

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        data = self.cleaned_data
        emp_code = data['emp_code']
        reg_empcode = '^LTPL-[0-9]{4}'
        if not re.match(reg_empcode, emp_code):
            self.errors['emp_code'] = ['Invalid emp code']