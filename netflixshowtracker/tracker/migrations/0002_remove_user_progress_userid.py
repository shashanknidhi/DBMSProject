# Generated by Django 4.0.5 on 2022-06-13 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_progress',
            name='userid',
        ),
    ]
