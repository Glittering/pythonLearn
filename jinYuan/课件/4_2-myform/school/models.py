from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 30,help_text= ('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'))
    age = models.IntegerField()
    gender = models.CharField(max_length = 10)

class Hobby(models.Model):
    name = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.name

# Create your models here.
