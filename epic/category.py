from django.db import models


class Category(models.Model):

	name = models.CharField(max_length=50)
	url = models.URLField(max_length=250, null=True, blank=True)



	def __str__(self):
		return self.name
