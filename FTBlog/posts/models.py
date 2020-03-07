from django.db import models

# Create your models here.

class Users(models.Model):
    logid = models.BigAutoField(db_column='LogId', primary_key=True)
    email = models.EmailField(db_column='Email', null=True, blank=True, unique=True)
    name = models.CharField(db_column='Name', max_length=15, blank=True)
    password = models.TextField(db_column='Password')    
    markedfordeletion = models.BooleanField(db_column='MarkedForDeletion', default=False)
    firstname = models.CharField(db_column='FirstName', max_length=30, blank=True)
    lastname = models.CharField(db_column='LastName', max_length=30, blank=True)


class Posts:
    pass

class comments:
    pass