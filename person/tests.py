# -*- coding: utf8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from person.models import Person
from datetime import date

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class HttpTest(TestCase):
    def setUp(self):
        self.person = Person.objects.create(
            firstname = u'Firstname',
            lastname = u'Lastname',
            birthday = date.today(),
            bio = u'biodata',
            email = u'email@example.com',
            jabber = u'jabber@example.com',
            skype = u'skype_login',
            other = u'Other contact data'
        )

    def test_personView(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '42 Coffee Cups Test Assignment')
        self.assertContains(response, self.person.firstname)
        self.assertContains(response, self.person.lastname)
        self.assertContains(response, self.person.email)