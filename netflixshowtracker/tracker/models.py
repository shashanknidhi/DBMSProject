from django.db import models

# Create your models here.
class show(models.Model):
    show_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    season = models.IntegerField()
    episodes = models.IntegerField()

class user_progress(models.Model):
    userid = models.CharField(max_length=30)
    show_name = models.CharField(max_length=255)
    season = models.IntegerField()
    episodes = models.IntegerField()
