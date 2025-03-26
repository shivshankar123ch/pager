from django.db import models
from django.db.models.base import Model



# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    certificate=models.CharField(max_length=60)
    Proficiency=models.TextField()
    auther=models.CharField(max_length=15)
    imag=models.ImageField(upload_to='cirtificate',blank=True,null=True)
    

    def __str__(self):
        return self.certificate

class Internship(models.Model):
    
    fullname=models.CharField(max_length=60)
    usn = models.CharField(max_length=10)
    email=models.CharField(max_length=60)
    phonenumber = models.CharField(max_length=10,null=True, blank=False)
    college_name=models.CharField(max_length=100)
    offer_status=models.CharField(max_length=60)
    start_date=models.CharField(max_length=60)
    end_date=models.CharField(max_length=60)
    proj_report=models.CharField(max_length=60)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    my_file=models.FileField(upload_to='',default=True)
    def __str__(self):
        
        return self.usn


