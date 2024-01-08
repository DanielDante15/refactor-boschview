from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile/',blank=True,null=True)
    stack = models.CharField(max_length=50,null=True,blank=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Project(models.Model):
    project_name = models.CharField(max_length=50,null=True)
    students = models.ManyToManyField(User, related_name='projects',null=True,blank=True)
    area = models.CharField(max_length=50,null=True)
    course = models.CharField(max_length=50,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255,null=True)
    techs = models.CharField( max_length=255,null=True)
    contact = models.CharField( max_length=255,null=True)
    finish_ratio = models.IntegerField(null=True)
    status = models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True,upload_to='projects/')
    price = models.DecimalField(decimal_places=2,max_digits=12,null=True,blank=True)
    proposal = models.TextField(null=True,blank=True)
    outside_scope_items = models.CharField(max_length=255,null=True,blank=True)
    requirements = models.TextField(null=True,blank=True)
    

    def __str__(self):
    	return self.project_name
    
