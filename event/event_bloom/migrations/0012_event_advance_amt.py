# Generated by Django 5.0.7 on 2024-09-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_bloom', '0011_event_remove_book_event_event_remove_book_event_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='advance_amt',
            field=models.IntegerField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
