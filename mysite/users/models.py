from django.db import models
from django.contrib.auth.models import User
DEFAULT_AUTO_FIELD='django.db.models.AutoField' 

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    loaction=models.CharField(max_length=300)
    def __str__(self):
        return self.user.username