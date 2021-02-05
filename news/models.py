from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import datetime
import pytz


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    posted_on = models.DateTimeField(default=datetime.datetime.now())
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return f"/news/{self.id}/"

    def get_short_decription(self):
        return self.desc[0:95] + "..."

    def get_time_difference(self):
        utc = pytz.UTC
        start_time = self.posted_on.replace(microsecond=0).replace(tzinfo=utc)
        end_time = datetime.datetime.now().replace(microsecond=0).replace(tzinfo=utc)
        time_difference = end_time - start_time

        return time_difference


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    posted_on = models.DateTimeField(default=datetime.datetime.now())
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def get_time_difference(self):
        utc = pytz.UTC
        start_time = self.posted_on.replace(microsecond=0).replace(tzinfo=utc)
        end_time = datetime.datetime.now().replace(microsecond=0).replace(tzinfo=utc)
        time_difference = end_time - start_time

        return time_difference
