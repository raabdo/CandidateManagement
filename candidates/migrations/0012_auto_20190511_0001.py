# Generated by Django 2.2 on 2019-05-10 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0011_auto_20190510_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='cv',
            field=models.FileField(upload_to='Cvs/%Y/<django.db.models.fields.CharField>'),
        ),
    ]
