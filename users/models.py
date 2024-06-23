from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class RequestLog(models.Model):
    path = models.CharField(max_length=1024)
    method = models.CharField(max_length=32)
    client_ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null = True, blank = True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.method} {self.path} by {self.user} at {self.timestamp}'