# Generated by Django 4.2.1 on 2023-05-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DogShow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DogShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('city', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=256)),
                ('range', models.IntegerField(choices=[(1, 'wojewódzka'), (2, 'krajowa'), (3, 'międzynarodowa')])),
            ],
        ),
    ]
