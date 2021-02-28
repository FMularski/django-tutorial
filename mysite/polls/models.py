from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=255, null=False)
    pub_date = models.DateTimeField('date published')   # human-readable name

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=False)
    votes = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.text