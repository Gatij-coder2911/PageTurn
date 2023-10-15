from django.db import models

# Create your models here.
class UsedBooks(models.Model):
    image=models.ImageField(upload_to="pics")
    category=models.CharField(max_length=100)
    price=models.FloatField(max_length=100)

    def __str__(self):
        return self.category

class RegisteredUsers(models.Model):
    full_name=models.CharField(max_length=100)
    
    mobile_no=models.BigIntegerField()
    email=models.EmailField(unique=True)

    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username
