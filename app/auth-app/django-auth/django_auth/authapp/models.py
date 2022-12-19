from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AppUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=1)

    def __str__(self):
        return 'User: {}, access level: {}'.format(self.user, self.access_level)
