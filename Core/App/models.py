from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
from .managers import CustomUserManager

class CustomUserModel(AbstractUser):
    first_name = None
    last_name = None

    dob= models.DateField(blank=True , null=True)
    email = models.EmailField(_("email address"), unique=True)
    modifiedAt = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Paragraph(models.Model):
    paragraph = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    def __str__(self):
        return f"Paragraph {self.id}"
    
class WordsTokanize(models.Model):
    word = models.CharField(max_length= 200 , blank=True)
    occurrence = models.IntegerField(default=0)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
