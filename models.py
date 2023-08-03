from django.db import models

# Create your models here.
class Trainee(models.Model):
    #trainee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    date_of_birth = models.DateField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name 


