# Generated by Django 2.2.10 on 2020-03-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200308_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]