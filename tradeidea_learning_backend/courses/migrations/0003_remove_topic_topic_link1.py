# Generated by Django 3.0.2 on 2020-02-07 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_topic_topic_link1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='topic_link1',
        ),
    ]
