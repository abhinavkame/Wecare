from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=10,null=True)
    


    def __str__(self):
        return self.user.username

class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=30)
    branch = models.CharField(max_length=10)
    subject = models.CharField(max_length=30)
    notesfile = models.FileField(max_length=30,null=True)
    filetyoe = models.CharField(max_length=10)
    state = models.CharField(max_length=100,blank=True, default=None)
    city = models.CharField(max_length=100,blank=True, default=None)
    description = models.CharField(max_length=300)
    status = models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return self.user.username+" "+self.status

class DonateFund(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    donatefund = models.IntegerField(null=True)
    