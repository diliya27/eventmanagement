# Generated by Django 5.0.7 on 2024-10-15 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_bloom', '0013_payment_book_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='order_id',
            new_name='book_id',
        ),
    ]
