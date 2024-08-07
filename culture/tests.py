from django.test import TestCase
from .models import Culture

class CultureTestCase(TestCase):
    def setUp(self):
        Culture.objects.create(name="tomate")

    def test_culture_was_created(self):
        culture = Culture.objects.get(name="tomate")
        self.assertEqual(culture.name, 'tomate')
        
    def test_culture_error_without_name(self):
        response = self.client.post('/api/cultures/', {'name': ''})
        self.assertEqual(response.status_code, 400)
    