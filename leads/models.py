from django.db import models
# creation of a custom folder
from django.contrib.auth.models import AbstractUser 

# from django.contrib.auth import get_user_model
# # kind of default user
# User = get_user_model() 
# YOU HAVE TO CREATE YOUR OWN CUSTOM USER CREATED, NOT GOOD TOU USE BUILT IN
class User(AbstractUser):
    pass
    # if we want to add another fields- remove pass and add any line you want



# Agent is person manages ou leads
class Agent(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Not the beswt practice to use foreign key
    # Another solution is available
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255) # can remove it because already have it on line class ''User(AbstractUser):pass''
    # built in user model
    
    
    

class Lead(models.Model):
    # Source choices stands for from where a user have learned about us
    # SOURCE_CHOICES = (
    #     ('YouTube','YouTube'),
    #     ('Google','Google'),
    #     ('Newsletter','Newsletter')
    # )
    
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    
    # Creating a foreign key Lead(belongs to) Agent
    # it is right to assign a foreign key in leads, showing that many leads, can have 1 manager
    #  maybe vice versa is also possible
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)
    
