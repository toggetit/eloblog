from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

class Entry(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = RichTextField('Содержание')
    #text = models.TextField()
    cdate = models.DateTimeField('Дата публикации', auto_now_add=True)
    edate = models.DateTimeField('Дата правки', auto_now=True)
    isDraft = models.BooleanField('Черновик', default=True)

    def __str__(self):
        return self.title
