# Generated by Django 2.2.10 on 2020-03-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200308_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
