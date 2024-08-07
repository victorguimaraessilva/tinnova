import json
from culture.models import Culture
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, **options):
        with open('culture/cultures.json', encoding='utf-8') as f:
            data = json.load(f)
            for culture in data['cultures']:
                try:
                    Culture.objects.get(name=culture['name'])
                except Exception:
                   
                    culture = Culture(
                        name = culture['name'],
                    )
                    culture.save()

            f.close()