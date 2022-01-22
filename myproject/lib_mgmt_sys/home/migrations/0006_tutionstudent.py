# Generated by Django 4.0 on 2021-12-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_authorpenname'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutionStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=244)),
                ('booked', models.ManyToManyField(to='home.Books')),
            ],
        ),
    ]
