# Generated by Django 3.0.4 on 2022-03-15 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0022_auto_20210416_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='display_title',
            field=models.CharField(default='', max_length=300),
        ),
    ]
