from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Client(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	def natural_key(self):
		return self.name

class Project(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	date_created = models.DateTimeField('date created', auto_now_add=True)
	client = models.ForeignKey(Client)
	vendor = models.ForeignKey(User,related_name='vendor')
	administrator = models.ForeignKey(User,related_name='administrator')
	status = models.PositiveIntegerField()

	def __str__(self):
		return self.name

class Item(models.Model):
	part_number = models.CharField(max_length=50, unique=True)
	brand = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	category = models.CharField(max_length=30)

	def __str__(self):
		return self.part_number

class Supplier(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	phone = models.PositiveIntegerField()
	email = models.EmailField()
	contact = models.CharField(max_length=50)
	items = models.ManyToManyField(Item, through='Cost')

	def __str__(self):
		return self.name

	def natural_key(self):
		return self.name

class Cost(models.Model):
	item = models.ForeignKey(Item)
	supplier = models.ForeignKey(Supplier)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	date_created = models.DateTimeField('date_created', auto_now=True)
	unit = models.CharField(max_length=8)

	def __str__(self):
		return self.price

class Requisition(models.Model):
	project = models.ForeignKey(Project)
	created_by = models.ForeignKey(User)
	supplier = models.ForeignKey(Supplier)
	coin = models.CharField(max_length=3)
	supplier_is_unique = models.BooleanField()
	status = models.PositiveIntegerField()
	date_authorized = models.DateTimeField('date_authorized', auto_now=True)
	date_buyed = models.DateTimeField('date_buyed', auto_now=True)
	requested_items = models.ManyToManyField(Item, through='RequestItem')

	def __str__(self):
		return self.pk

class RequestItem(models.Model):
	requisition = models.ForeignKey(Requisition)
	item = models.ForeignKey(Item)
	quantity = models.PositiveSmallIntegerField()
	date_required = models.DateTimeField('date_required')
	date_arrived = models.DateTimeField('date_arrived')

	def __str__(self):
		return self.id