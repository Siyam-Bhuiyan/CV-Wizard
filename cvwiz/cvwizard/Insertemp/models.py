from django.db import models

class dbins(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.TextField()
    education=models.TextField()
    experience=models.TextField()
    class Meta():
        db_table= "cv_information"