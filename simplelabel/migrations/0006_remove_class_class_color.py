# Generated by Django 3.2.15 on 2022-08-19 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplelabel', '0005_class_class_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='class_color',
        ),
    ]
