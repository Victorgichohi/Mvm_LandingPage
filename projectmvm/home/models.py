from django.db import models

# Create your models here.

class Student(models.Model):
	full_name = models.CharField(max_length=200)
	age=models.IntegerField()
	email=models.EmailField()
	interests=models.TextField()
	registered_date=models.DateField(auto_now=False, auto_now_add=True)
	last_update=models.DateField(auto_now=True, auto_now_add=False)

	def _str_(self):
		return self.full_name

class Classroom(models.Model):
	full_name=models.CharField(max_length=200)
	floor=models.CharField(max_length=200)
	has_podium=models.BooleanField(initial=True)
	commissioned_date=models.DateField(auto_now=False, auto_now_add=True)
	created_at=models.DateField(auto_now=False, auto_now_add=True)
	updated_at=models.DateField(auto_now=True, auto_now_add=False)

	