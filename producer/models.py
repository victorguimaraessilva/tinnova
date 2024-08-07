from django.db import models
from django.core.exceptions import ValidationError  
from django_softdelete.models import SoftDeleteModel
from culture.models import Culture
from .validators import validate_document

class Producer(SoftDeleteModel):

    class Meta:
        ordering = ["id"]
        verbose_name = 'Produto Rural'
        verbose_name_plural = 'Produtores Rurais'


    def __str__(self):
        return str(self.producer_name)

    id = models.BigAutoField(primary_key=True)
 
    cultures = models.ManyToManyField(Culture, verbose_name='Culturas')

    document = models.CharField(verbose_name='CPF/CNPJ', max_length=14, null=False, blank=False, validators=[validate_document])
    
    producer_name = models.CharField(verbose_name='Produtor', max_length=150, null=False, blank=False)
    
    farm_name = models.CharField(verbose_name='Fazenda', max_length=150, null=False, blank=False)
    
    city = models.CharField(verbose_name='Cidade', max_length=100, null=False, blank=False)
    
    state = models.CharField(verbose_name='Estado', max_length=50, null=False, blank=False)
    
    total_area = models.FloatField(verbose_name='Área Total', blank=False, null=False)
    
    arable_area = models.FloatField(verbose_name='Área Agriculturável', blank=False, null=False)
    
    vegetation_area = models.FloatField(verbose_name='Área de Vejetação', blank=False, null=False)
    
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True, editable=False, blank=True, null=True)
    
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True, editable=False, blank=True, null=True)
 
    def clean(self):      
        if self.total_area < self.arable_area + self.total_area:
            raise ValidationError(
                {'total_area': ('A soma de área agrícultável e vegetação, não deverá ser maior que a área total da fazenda.')}
            )