from django.shortcuts import render
from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm , DepartmentForm, MyForm
from employee.models import Employee , Department, Model1, Model2
 
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")

def create_emp(request):  
    if request.method == "POST":  
        form = MyForm(request.POST)
        if form.is_valid():
            # Create instances of both models
            model1_instance = Model1.objects.create(
                field1=form.cleaned_data['field1'],
                field2=form.cleaned_data['field2']
            )
            model2_instance = Model2.objects.create(
                model1=model1_instance,
                field3=form.cleaned_data['field3'],
                field4=form.cleaned_data['field4']
            )
            # Save instances to the database
            model1_instance.save()
            model2_instance.save()
            return render(request, 'show.html')
    else:
        form = MyForm()
    return render(request, 'create.html', {'form': form})