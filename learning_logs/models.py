from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    title = models.CharField(default=None, max_length=80)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        if len(self.text) > 50: return self.text[:50] + "..."
        else: return self.text