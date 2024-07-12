# Generated by Django 5.0.6 on 2024-07-11 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap3', '0003_meeting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptopic', models.CharField(max_length=200)),
                ('planguage', models.CharField(max_length=200)),
                ('pduration', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ap3.student')),
            ],
        ),
    ]
