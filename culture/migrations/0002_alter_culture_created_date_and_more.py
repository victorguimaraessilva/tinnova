# Generated by Django 5.0.8 on 2024-08-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culture',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='culture',
            name='deleted_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Deletado em'),
        ),
        migrations.AlterField(
            model_name='culture',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='culture',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em'),
        ),
    ]
