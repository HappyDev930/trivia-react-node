# Generated by Django 3.0.2 on 2020-02-19 15:29

import courses.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20200219_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='exam_pass',
            field=courses.models.IntegerRangeField(default=0),
            preserve_default=False,
        ),
    ]
