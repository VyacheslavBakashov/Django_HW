# Generated by Django 4.1.3 on 2022-11-24 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['-status', 'created_at']},
        ),
    ]
