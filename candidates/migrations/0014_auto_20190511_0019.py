# Generated by Django 2.2 on 2019-05-10 16:19

import candidates.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0013_auto_20190511_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='cv',
            field=models.FileField(upload_to=candidates.models.get_upload_path),
        ),
    ]
