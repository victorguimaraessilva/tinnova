# Generated by Django 5.0.8 on 2024-08-07 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('culture', '0002_alter_culture_created_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='culture',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='culture',
            old_name='updated_date',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='deleted_date',
        ),
    ]