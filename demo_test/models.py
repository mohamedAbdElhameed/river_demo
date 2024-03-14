from django.db import models
from river.models.fields.state import StateField


# Create your models here.
class Stage(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()
    my_state_field = StateField()

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()
    my_state_field = StateField()

    def __str__(self):
        return self.name
