"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from .views import WelcomeView, AboutUsView


class UrlTests(TestCase):
    def test_welcome_url(self):
        """Tests when we go to the welcome url it loads the welcome view"""
        welcome = resolve(reverse('checkunits:welcome'))
        return self.assertEqual(welcome.func.__name__,
                                WelcomeView.__name__)
# this test above helps to check for bad pattern matching


class AboutUs(TestCase):
    def test_aboutus_url(self):
        """Tests when we go to the welcome url it loads the welcome view"""
        aboutus = resolve(reverse('checkunits:aboutus'))
        return self.assertEqual(aboutus.func.__name__,
                                AboutUsView.__name__)


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
