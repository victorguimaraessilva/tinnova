import json
from culture.models import Culture
from producer.models import Producer
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, **options):
        with open('producer/producers.json', encoding='utf-8') as f:
            data = json.load(f)
            for producer in data['producers']:
                try:
                    Producer.objects.get(document=producer['document'])
                except Exception:
                    
                    cultures = Culture.objects.filter(pk__in=producer['cultures'])
                   
                    producer = Producer(
                        document = producer['document'],
                        producer_name = producer['producer_name'],
                        farm_name = producer['farm_name'],
                        city = producer['city'],
                        state = producer['state'],
                        total_area = producer['total_area'],
                        arable_area = producer['arable_area'],
                        vegetation_area = producer['vegetation_area']
                    )
                    
                    producer.save()
                    
                    producer.cultures.set(cultures)

            f.close()