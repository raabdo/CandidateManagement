# Generated by Django 2.2 on 2019-05-09 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0002_auto_20190509_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview',
            old_name='name',
            new_name='candidate',
        ),
    ]
