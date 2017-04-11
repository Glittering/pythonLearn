from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    gender = models.CharField(max_length = 10)
    subject = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-name']
# Create your models here.
