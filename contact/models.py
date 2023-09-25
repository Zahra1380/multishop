from django.db import models


class Massage(models.Model):
    neme = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    massage = models.TextField()

    def __str__(self):
        return self.subject