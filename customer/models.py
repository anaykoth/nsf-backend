from django.db import models

class Customer(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    occupation = models.CharField(max_length=50)
    feedback = models.CharField(max_length=1000)

    def __str__(self):
        return self.firstName
