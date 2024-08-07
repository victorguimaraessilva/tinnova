from django.test import TestCase
from .models import Producer

class ProducerTestCase(TestCase):
    
    def setUp(self):
        Producer.objects.create(
            document="06744087053",
            producer_name="producer",
            farm_name="farm",
            city="city",
            state="state",
            total_area=100,
            arable_area=50,
            vegetation_area=50
        )

    def test_culture_was_created(self):
        producer = Producer.objects.get(document="06744087053")
        self.assertEqual(producer.document, '06744087053')
        self.assertEqual(producer.producer_name, 'producer')
        self.assertEqual(producer.farm_name, 'farm')
        self.assertEqual(producer.city, 'city')
        self.assertEqual(producer.state, 'state')
        self.assertEqual(producer.total_area, 100)
        self.assertEqual(producer.arable_area, 50)
        self.assertEqual(producer.vegetation_area, 50)
    
    def test_producer_error_without_producer_document(self):
        response = self.client.post('/api/producers/', {'document': ''})
        self.assertEqual(response.status_code, 400)
        
    def test_producer_error_without_producer_name(self):
        response = self.client.post('/api/producers/', {'producer_name': ''})
        self.assertEqual(response.status_code, 400)
        
    def test_producer_error_without_producer_farm_name(self):
        response = self.client.post('/api/producers/', {'farm_name': ''})
        self.assertEqual(response.status_code, 400)
        
    def test_producer_error_without_producer_city(self):
        response = self.client.post('/api/producers/', {'city': ''})
        self.assertEqual(response.status_code, 400)
        
    def test_producer_error_without_producer_state(self):
        response = self.client.post('/api/producers/', {'state': ''})
        self.assertEqual(response.status_code, 400)
        
    def test_producer_error_without_producer_total_area(self):
        response = self.client.post('/api/producers/', {'total_area': ''})
        self.assertEqual(response.status_code, 400)
        
    def test_producer_error_without_producer_arable_area(self):
        response = self.client.post('/api/producers/', {'arable_area': ''})
        self.assertEqual(response.status_code, 400)
        
    def test_producer_error_without_producer_vegetation_area(self):
        response = self.client.post('/api/producers/', {'vegetation_area': ''})
        self.assertEqual(response.status_code, 400)
    
    def test_producer_error_with_invalid_document(self):
        response = self.client.post('/api/producers/', {
            "document": "86278948091",
            "producer_name": "producer",
            "farm_name": "farm",
            "city": "city",
            "state": "state",
            "total_area": 150.0,
            "arable_area": 50.0,
            "vegetation_area": 100.0,
            "cultures": []
        })
        self.assertEqual(response.status_code, 400)
        
    def test_producer_error_with_invalid_areas(self):
        response = self.client.post('/api/producers/', {
            "document": "86278948095",
            "producer_name": "producer",
            "farm_name": "farm",
            "city": "city",
            "state": "state",
            "total_area": 100.0,
            "arable_area": 250.0,
            "vegetation_area": 100.0,
            "cultures": []
        })
        self.assertEqual(response.status_code, 400)