from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1500)
    time = models.DateTimeField(auto_now_add=True)
    messagelooked = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('time',)
