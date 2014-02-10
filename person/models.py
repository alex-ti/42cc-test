# -*- coding: utf8 -*-
from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=70, verbose_name=u'name')
    lastname = models.CharField(max_length=70)
    birthday = models.DateField(verbose_name=u'date of birth')
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=32)
    other = models.TextField()

    def __unicode(self):
        return u'%s %s' % (self.firstname, self.lastname)