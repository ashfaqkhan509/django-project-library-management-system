# Generated by Django 5.0.6 on 2024-08-17 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_remove_book_is_available_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='member',
        ),
        migrations.AlterField(
            model_name='issuebook',
            name='expired_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 1, 14, 18, 5, 445324)),
        ),
    ]
