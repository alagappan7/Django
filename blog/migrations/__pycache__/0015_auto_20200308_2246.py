# Generated by Django 2.2.10 on 2020-03-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('Department', models.CharField(blank=True, max_length=70, null=True)),
                ('mailid', models.EmailField(blank=True, max_length=254, null=True)),
                ('writeuperrors', models.IntegerField(blank=True, null=True)),
                ('text', models.TextField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
