# Generated by Django 5.0.7 on 2024-09-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_bloom', '0004_service_outline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField(max_length=10)),
                ('email', models.TextField(max_length=50)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
