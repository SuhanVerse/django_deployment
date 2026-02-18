from django.test import TestCase
from .utils import add
from django.urls import reverse


class AddFunctionTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)


class RegistrationFormPageTestCase(TestCase):
    def test_registration_contains_input_text(self):
        response = self.client.get(reverse('registration:form'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Password:')

