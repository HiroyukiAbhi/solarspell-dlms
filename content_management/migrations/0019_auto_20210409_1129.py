# Generated by Django 3.0.4 on 2021-04-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0018_content_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='file_name',
            field=models.CharField(max_length=500),
        ),
    ]
