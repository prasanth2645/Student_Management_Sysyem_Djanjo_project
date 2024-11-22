from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True,null=True)
    address=models.CharField(max_length=255,blank=True,null=True)
    date_of_birth=models.DateField(null=True,blank=True)




class Sample(models.Model):
    name=models.CharField(max_length=10,blank=False,null=False)#blank=True not req field ,if blank=Flase means req
    date=models.DateField(auto_now=True)
    is_active=models.BooleanField()#defalt=True
    description=models.TextField(max_length=500,blank=True,null=True)
    price=models.FloatField()
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    appointment_time=models.TimeField(auto_now=True)
    email=models.EmailField(max_length=30)
    url=models.URLField()
    file=models.FileField(upload_to="file/")
    image=models.ImageField(upload_to="image/")

#onetoone field
class Person(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=10)
class Profile(models.Model):
    user=models.OneToOneField(Person,on_delete=models.CASCADE)
    bio=models.CharField(max_length=50)
    birthdate=models.DateField(blank=True,null=True)

#onetomany field
class Department(models.Model):
    name=models.CharField(max_length=100)
class Std(models.Model):
    name=models.CharField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

#manytomany
class Courses(models.Model):
    name = models.CharField(max_length=15)
class Emp(models.Model):
    title = models.CharField(max_length=25)
    course= models.ManyToManyField(Courses,max_length=15)






