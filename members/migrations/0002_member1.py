# Generated by Django 5.1.1 on 2024-09-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname1', models.CharField(max_length=255)),
                ('lastname2', models.CharField(max_length=255)),
            ],
        ),
    ]
