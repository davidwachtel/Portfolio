from django.db import models

# Create your models here.
from django.utils.timezone import now


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=now)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title