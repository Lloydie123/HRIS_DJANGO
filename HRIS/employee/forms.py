from django import forms  
from employee.models import Employee, Department, Model1, Model2
from django.forms import fields

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  

class DepartmentForm(forms.ModelForm):  
    class Meta:  
        model = Department
        fields =  ('dep_name',)

class MyForm(forms.Form):
    field1 = forms.CharField(max_length=50)
    field2 = forms.CharField(max_length=50)
    field3 = forms.CharField(max_length=50)
    field4 = forms.CharField(max_length=50)