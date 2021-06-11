from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Form(models.Model):
    c_fname=models.CharField(max_length=50)
    c_lname=models.CharField(max_length=45)
    c_email=models.CharField(max_length=50)
    c_subject=models.CharField(max_length=45)
    c_message=models.CharField(max_length=30)

    def __str__(self):
     return self.c_fname
