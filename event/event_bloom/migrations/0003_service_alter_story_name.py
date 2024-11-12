# Generated by Django 5.0.7 on 2024-08-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_bloom', '0002_story_outline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='story',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]