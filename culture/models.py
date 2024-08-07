from django.db import models
from django_softdelete.models import SoftDeleteModel


class Culture(SoftDeleteModel):

    class Meta:
        ordering = ["name"]
        verbose_name = 'Cultura de Plantio'
        verbose_name_plural = 'Culturas de Plantio'


    def __str__(self):
        return str(self.name)

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(verbose_name='Nome', max_length=150, null=False, blank=False)
    
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True, editable=False, blank=True, null=True)
    
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True, editable=False, blank=True, null=True)
