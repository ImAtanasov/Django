from django.db import models

class apartment_sell(models.Model):
	location = models.CharField('Location', max_length=120)
	date = models.DateTimeField('Post Date')
	venue = models.CharField(max_length=120)
	person = models.CharField(max_length = 60)
	description = models.TextField(blank=True)
	
class apartment_buy(models.Model):
	location = models.CharField('Location', max_length=120)
	date = models.DateTimeField('Post Date')
	venue = models.CharField(max_length=120)
	person = models.CharField(max_length = 60)
	description = models.TextField(blank=True)

class rent_sell(models.Model):
	location = models.CharField('Location', max_length=120)
	date = models.DateTimeField('Post Date')
	venue = models.CharField(max_length=120)
	person = models.CharField(max_length = 60)
	description = models.TextField(blank=True)
	
class rent_buy(models.Model):
	location = models.CharField('Location', max_length=120)
	date = models.DateTimeField('Post Date')
	venue = models.CharField(max_length=120)
	person = models.CharField(max_length = 60)
	description = models.TextField(blank=True)