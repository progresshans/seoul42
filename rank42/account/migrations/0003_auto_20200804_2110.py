# Generated by Django 2.2.13 on 2020-08-04 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_myuser_can_see_piscine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='can_see_piscine',
            new_name='allow_piscine_list',
        ),
    ]
