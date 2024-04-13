from django.contrib import admin
from .models import CustomUserModel, Paragraph, WordsTokanize

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(Paragraph)
admin.site.register(WordsTokanize)