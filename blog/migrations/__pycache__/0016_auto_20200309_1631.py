# Generated by Django 2.2.10 on 2020-03-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200308_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='Fathername',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='collegeid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='collegename',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='Department',
            field=models.CharField(choices=[('cse', 'CSE'), ('ece', 'ECE'), ('it', 'IT'), ('mech', 'MECH'), ('civil', 'CIVIL')], default='cse', max_length=70),
        ),
    ]
