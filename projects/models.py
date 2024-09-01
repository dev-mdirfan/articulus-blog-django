from django.db import models

class Project(models.Model):
    
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='projects/thumbnail/' + '%Y/%m/%d/', default='projects/thumbnail/default.png')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title