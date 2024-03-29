from django.db import models

class Host(models.Model):
    hostname    = models.CharField(max_length=100)
    hostloc     = models.TextField()

    def __str__(self):
        return "%s %s " %(self.hostname, self.hostloc)