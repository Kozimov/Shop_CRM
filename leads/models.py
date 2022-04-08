from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class UserProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)

class Lead(models.Model):
    ismi = models.CharField(max_length=20)
    familiyasi = models.CharField(max_length=20)
    yoshi = models.IntegerField(default=0)
    seller = models.ForeignKey("Seller", on_delete=models.CASCADE)

    def __str__(self):
        return self.ismi


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profil = models.ForeignKey(UserProfil, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)