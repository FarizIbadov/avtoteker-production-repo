from django.db import models

class Email(models.Model):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email

class AuthUser(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
