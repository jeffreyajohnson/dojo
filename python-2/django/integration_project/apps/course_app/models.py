from __future__ import unicode_literals

from django.db import models
from ..login_reg_app.models import User

class Course(models.Model):
	catalogNo = models.SmallIntegerField()
	name = models.CharField(max_length=45)
	description = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	users = models.ManyToManyField(User)
	


