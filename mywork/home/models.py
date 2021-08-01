from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name



class Signup(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name        




class Books(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    about = models.TextField(max_length=1000) 
    fileUrl = models.TextField(max_length=1000)
    posterUrl = models.TextField(max_length=1000)
    category = models.CharField(max_length=50)
    isForMembers = models.BooleanField(default=True)
    class Meta:
        db_table = 'books'
    
    

