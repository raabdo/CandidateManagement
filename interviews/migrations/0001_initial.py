# Generated by Django 2.2 on 2019-05-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('booked', models.BooleanField()),
                ('name', models.ForeignKey(on_delete=True, to='candidates.candidate')),
            ],
        ),
    ]
