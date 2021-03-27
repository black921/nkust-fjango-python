from django.db import models
from django.utils import timezone



class Post(models.Model):
	title = models.CharField(max_length=200)
	vid = models.CharField(max_length=20,default="9zcgSJBplsQ")
	pub_date = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-pub_date',)

	def __str__(self):
		return self.title

# Create your models here.
