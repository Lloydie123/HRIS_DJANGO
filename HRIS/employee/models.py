from django.db import models  

class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15) 

    def __str__(self):
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "employee"  


class Department(models.Model):  
   
    dep_name = models.CharField(max_length=100)  
   

    def __str__(self):
        return "%s " %(self.depname) 
    class Meta:  
        db_table = "department"  

class Model1(models.Model):
    field1 = models.CharField(max_length=50)
    field2 = models.CharField(max_length=50)

class Model2(models.Model):
    model1 = models.ForeignKey(Model1, on_delete=models.CASCADE)
    field3 = models.CharField(max_length=50)
    field4 = models.CharField(max_length=50)