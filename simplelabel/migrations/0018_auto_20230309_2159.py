# Generated by Django 3.2.18 on 2023-03-09 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplelabel', '0017_auto_20230309_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('image',)},
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_name',
        ),
    ]
