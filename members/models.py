from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Member1(models.Model):
  firstname1 = models.CharField(max_length=255)
  lastname2 = models.CharField(max_length=255)