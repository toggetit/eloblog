from django.db import models

# Create your models here.
from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField

class Entry(models.Model):
    title = models.CharField(max_length=200)
    #text = tinymce_models.HTMLField()
    text = RichTextField()
    cdate = models.DateTimeField('Дата публикации', auto_now_add=True)
    edate = models.DateTimeField('Дата правки', auto_now=True)

    def __str__(self):
        return self.title
