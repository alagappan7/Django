# Generated by Django 2.2.10 on 2020-03-07 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_commque_techque'),
    ]

    operations = [
        migrations.AddField(
            model_name='commque',
            name='response',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='techque',
            name='response',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]