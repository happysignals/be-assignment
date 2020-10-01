from uuid import uuid4

from django.db import models
from django.contrib.admin import site

def make_uuid():
  return uuid4().hex


class Factor(models.Model):
  slug = models.SlugField(default=make_uuid)
  title = models.CharField(max_length=200)

  def __str__(self):
    return f"{self.title}"

class Survey(models.Model):
  slug = models.SlugField(default=make_uuid)
  question = models.CharField(max_length=200)
  factors = models.ManyToManyField(Factor, related_name="survey")

  def __str__(self):
    return f"{self.question}"

class Response(models.Model):
  value = models.IntegerField(blank=False, null=False)
  comment = models.CharField(max_length=2000)
  factors = models.ManyToManyField(Factor, related_name="+")
