from django.db import models

class employeesm(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    emp_id=models.ImageField()

    def __str__(self):
        return self.firstname


# Create your models here.
