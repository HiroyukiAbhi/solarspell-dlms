# Generated by Django 3.0.4 on 2020-11-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0011_auto_20201118_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='rights_holder',
            new_name='additional_notes',
        ),
        migrations.AddField(
            model_name='content',
            name='original_source',
            field=models.TextField(null=True),
        ),
    ]
