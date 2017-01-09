from django.db import models
from django.core.urlresolvers import reverse
import sys


class Book(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField ()
    randNum = models.IntegerField()
    bizz = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_bizz:book_edit', kwargs={'pk': self.pk})
    