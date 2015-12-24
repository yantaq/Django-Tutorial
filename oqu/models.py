from django.db import models

# Create your models here.

class Quran(models.Model):
    database_id = models.CharField(max_length=5)
    sura_id = models.CharField(max_length=3)
    verse_id = models.CharField(max_length=3)
    ayat_text = models.TextField()
    
