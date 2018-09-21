from django.db import models
from django.contrib.auth.models import User


class Loginpage(models.Model):
    user = models.OneToOneField(User, on_delete='')
    name = models.CharField(max_length=200)
    Birthday = models.DateField()
    image = models.ImageField(upload_to='loginpage/media', blank=True)

    def __unicode__(self):
        return self.name




