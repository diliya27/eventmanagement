# Generated by Django 5.0.7 on 2024-08-08 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_bloom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='outline',
            field=models.TextField(default=123),
            preserve_default=False,
        ),
    ]
