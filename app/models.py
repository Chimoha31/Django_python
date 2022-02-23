from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title=models.CharField("Title", max_length=200)
  content = models.TextField("Content")
  created = models.DateTimeField("Date of Written", default=timezone.now)

  def __str__(self):
    return self.title
