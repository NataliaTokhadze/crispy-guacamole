# Generated by Django 5.1.2 on 2025-01-17 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meow', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Comment',
            new_name='comment',
        ),
    ]