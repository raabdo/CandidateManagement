# Generated by Django 2.2 on 2019-05-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='username',
            field=models.CharField(default='New user {pk}', max_length=10, unique=True),
        ),
    ]