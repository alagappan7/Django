# Generated by Django 2.2.10 on 2020-03-08 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_post_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='writeuperrors',
            new_name='Score',
        ),
    ]
