from django.db import models

"""
class Note
    title str
    contend str
    createdAt datetime
"""

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title 