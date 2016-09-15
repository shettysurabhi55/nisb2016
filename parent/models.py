from django.db import models
import datetime

# Create your models here.

# Bulletin/Tech news home page
class Bulletin(models.Model):
	subjectsTo_choices = (
			(0, "Branch"),
			(1, "Sectional"),
			(2, "Regional"),
			(3, "Interregional"),
			(4, "Misc"),
			)
	# Bulletin line
	theLine = models.TextField(null=False, unique=True)
	# Link to detailed information
	theLink = models.URLField(unique=True)
	subjectsTo = models.PositiveIntegerField(choices=subjectsTo_choices, null=False)

	def __str__(self):
		return self.theLine


# Events that have been/are/are to be hosted
class Events(models.Model):
	agInvolved = (
			(0, "None"),
			(1, "Computer Society"),
			(2, "WIE"),
			(4, "Focus Group"),
			)
	# To be followed as EVT-yr-no
	eventID = models.CharField(max_length=9, primary_key=True)
	# name
	eventName = models.TextField(max_length=45, null=False, default="Suggest")
	# Registration link
	regLink = models.URLField(unique=True)
	# Registration Deadline (if required add null=False as an argument)
	deadLine = models.DateField()
	#venue
	venue = models.TextField(max_length=20, default="To be updated")
	# Event start date
	eventDate = models.DateField(null=False)
	# Feedback link
	fbLink = models.URLField()
	ag = models.PositiveIntegerField(choices=agInvolved, null=False)
	# Event details
	info = models.TextField(null=False)
	# Pre-requisites, required resources etc
	requirements = models.TextField()

	def __str__(self):
		return self.eventID

# Member's details, more to be added
class User(models.Model):
	ieee_num = models.PositiveIntegerField(primary_key=True)
	name = models.TextField(max_length=40)
	isCS = models.BooleanField(default=False)
	memExpires = models.DateField(null=False)
	memCSExpires = models.DateField(null=False)
