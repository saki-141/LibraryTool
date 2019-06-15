from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=100)
    tag2 = models.CharField(max_length=100, blank=True)
    tag3 = models.CharField(max_length=100, blank=True)
    status = models.IntegerField()
    link = models.CharField(max_length=400)
    
    def __str__(self):
        return str(self.id) + ':' + self.title + ':' + self.author
    