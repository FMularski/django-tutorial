from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255, null=False)
    pub_date = models.DateTimeField('date published')   # human-readable name

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=False)
    votes = models.IntegerField(default=0, null=False)