from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='posts/thumbnail/' + '%Y/%m/%d/', default='posts/thumbnail/default.png')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now, editable=False)
    date_updated = models.DateTimeField(default=timezone.now, editable=True)

    def __str__(self):
        return self.title