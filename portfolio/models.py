from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False) # Time is save in db
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True) # When something is added for the first time, it's saved in db

def __unicode__(self):
	return self.title

def __str__(self):
	return self.title