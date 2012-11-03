from django.db import models

class UrlPair(models.Model):
    url = models.TextField()
    newUrl = models.TextField()

    def __unicode__(self):
        return self.newUrl + " => " + self.url
