from django.db import models

from django.db import models

class Marts(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
