# Generated by Django 2.2.2 on 2019-06-30 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_bookcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'categories'},
        ),
    ]