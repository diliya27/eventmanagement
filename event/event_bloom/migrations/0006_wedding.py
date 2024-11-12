# Generated by Django 5.0.7 on 2024-09-10 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_bloom', '0005_inform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]