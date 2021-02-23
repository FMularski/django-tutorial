from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=255, null=False)
    pub_date = models.DateTimeField('date published')   # human-readable name

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=False)
    votes = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.text