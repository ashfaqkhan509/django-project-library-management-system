# Generated by Django 5.0.6 on 2024-08-16 09:00

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('is_available', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=200, null=True, unique=True)),
                ('membership_date', models.DateTimeField(auto_now_add=True)),
                ('membership_status', models.CharField(choices=[('active', 'Active'), ('closed', 'Closed'), ('blacklist', 'Blacklist')], default='active', max_length=20)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_date', models.DateField(default=django.utils.timezone.now)),
                ('returned_date', models.DateField(blank=True, null=True)),
                ('expired_date', models.DateTimeField(default=datetime.datetime(2024, 8, 31, 14, 0, 36, 234376))),
                ('fine_per_day', models.PositiveIntegerField(default=0)),
                ('over_due', models.BooleanField(blank=True, default=False, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.member')),
            ],
        ),
    ]
