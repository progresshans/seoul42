# Generated by Django 3.1 on 2020-08-19 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_apikey'),
    ]

    operations = [
        migrations.AddField(
            model_name='apikey',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
