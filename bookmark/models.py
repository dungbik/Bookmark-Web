from django.db import models

from django.urls import reverse

class Bookmark(models.Model):
    siteName = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def __str__(self):
        return '이름 : ' + self.siteName + ", 주소 : " + self.url