# Generated by Django 3.1 on 2020-08-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_usertoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertoken',
            name='ft_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
