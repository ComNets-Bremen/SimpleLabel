# Generated by Django 3.2.16 on 2022-11-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplelabel', '0008_alter_class_class_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ('class_id',)},
        ),
        migrations.AddField(
            model_name='dataset',
            name='datase_active',
            field=models.BooleanField(default=True),
        ),
    ]
