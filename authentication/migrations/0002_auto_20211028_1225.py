# Generated by Django 3.2.8 on 2021-10-28 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notes',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
