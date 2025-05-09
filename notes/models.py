from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
