# Generated by Django 3.2.7 on 2022-07-19 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_sport'),
    ]

    operations = [
        migrations.CreateModel(
            name='electronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
