from django.db import models
from django.contrib.auth.models import AbstractUser

# Create model based on existing model.

# If you’re starting a new project, it’s highly recommended to set up a custom user model, 
# even if the default User model is sufficient for you. 
# This model behaves identically to the default user model, 
# but you’ll be able to customize it in the future if the need arises:

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous')  
    # if no name is given we can write default name as Anonymous
    email = models.EmailField(max_length=254, unique=True)
    
    # we don't want to signup on the basis of user name.
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    phone = models.CharField(max_length=50, blank=True, null=True)    
    gender = models.CharField(max_length=50, blank=True, null=True)    

    session_token = models.CharField(max_length=10, default=0)
    # default=0 means that the user is not login
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
        
