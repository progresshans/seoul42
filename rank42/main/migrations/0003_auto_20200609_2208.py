# Generated by Django 2.2.13 on 2020-06-09 22:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tier'),
    ]

    operations = [
        migrations.AddField(
            model_name='tier',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tier',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
