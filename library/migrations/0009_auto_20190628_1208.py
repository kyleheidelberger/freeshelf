# Generated by Django 2.2.2 on 2019-06-28 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20190628_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['full_name']},
        ),
    ]
