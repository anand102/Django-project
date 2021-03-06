from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Social(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=False, default=datetime.now())
	thumb = models.ImageField(default='default.png', blank=True)
	profile = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def snippet(self):
	    return self.body[:50] + '...'	