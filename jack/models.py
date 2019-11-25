# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Review(models.Model):
	reviewer = models.CharField(max_length=100)
	review = models.TextField()
	rating = models.CharField(max_length=100)
	date = models.DateField(auto_now=False, auto_now_add=False)
	positive = models.CharField(max_length=100, default='', blank=True, null=True)
	neutral = models.CharField(max_length=100, default='', blank=True, null=True)
	negative = models.CharField(max_length=100, default='', blank=True, null=True)
	word_count = models.IntegerField()
	month_average = models.CharField(max_length=100, default='', blank=True, null=True)

class Common_words(models.Model):
	word = models.CharField(max_length=100)
	frequency = models.IntegerField()
	rating = models.CharField(max_length=100)
	year = models.IntegerField()

class Average(models.Model):
	year = models.IntegerField()
	average = models.CharField(max_length=100)


# Create your models here.
