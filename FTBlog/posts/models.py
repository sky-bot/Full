from django.db import models

# Create your models here.

class Users(models.Model):
    userId = models.BigAutoField(db_column='UserId', primary_key=True)
    email = models.EmailField(db_column='Email', null=True, blank=True, unique=True)
    name = models.CharField(db_column='Name', max_length=30, blank=True)
    password = models.TextField(db_column='Password')    
    markedfordeletion = models.BooleanField(db_column='MarkedForDeletion', default=False)
    firstname = models.CharField(db_column='FirstName', max_length=30, blank=True)
    lastname = models.CharField(db_column='LastName', max_length=30, blank=True)

    class Meta:
        db_table = 'Users'

class UserPostMapping(models.Model):
    logid = models.BigAutoField(db_column='LogId', primary_key=True)
    userId = models.IntegerField(db_column='UserId')
    postId = models.IntegerField(db_column='PostId')

    class Meta:
        db_table = 'UserPostMapping'

class Posts(models.Model):
    postId = models.BigAutoField(db_column='PostId', primary_key=True)
    title =  models.TextField(blank = False, default='Anonymous User')
    subtitle = models.TextField(blank = False, default='--')
    author =  models.TextField(blank = False, default='--')
    posts = models.TextField(blank = False)
    createdAt =  models.DateTimeField(db_column="CreatedAt", blank=True, null=True)

    class Meta:
        db_table = 'Posts'
    

class Comments(models.Model):
    commentId = models.BigAutoField(db_column='CommentId', primary_key=True)
    comment = models.TextField(blank = False)
    createdAt =  models.DateTimeField(db_column="createdAt", blank=True, null=True)
    username = models.CharField(db_column='UserName', max_length=30, blank=True)

    class Meta:
        db_table = 'Comments'
    