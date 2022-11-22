from django.db import models

# Create your models here.
class APP(models.Model):
    ID=models.AutoField(primary_key=True)
    FIRST_NAME=models.CharField( max_length=50)
    LAST_NAME=models.CharField( max_length=50)
    EMAIL=models.EmailField( max_length=50)
    NUMBER=models.CharField( max_length=50)
    AGE=models.CharField( max_length=50)
    GENDER=models.CharField( max_length=50)

    
