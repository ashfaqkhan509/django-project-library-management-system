# Generated by Django 5.0.6 on 2024-08-19 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_alter_member_options_alter_member_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='expired_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 3, 16, 33, 30, 595669)),
        ),
    ]
