from django.db import models

class Role(models.Model):
	role_name = models.CharField(max_length=200)

	def __str__(self):
		return self.role_name

