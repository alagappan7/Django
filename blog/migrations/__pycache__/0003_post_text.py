# Generated by Django 2.2.10 on 2020-03-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200214_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
