from django.db import models

# Create your models here.

class Workout(models.Model):
    Date = models.DateField()
    Name = models.CharField(max_length=50)

class Exercise(models.Model):
    name = models.CharField(max_length=128)
    bodypart = models.CharField(max_length=128)
    reps = models.IntegerField()

class Set(models.Model):
    exercise = models.AutoField(queryset = Exercise, empty_label="(nothing)")
    Workout = models.ForeignKey(Workout, on_delete = models.CASCADE)
