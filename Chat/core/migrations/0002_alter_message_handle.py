# Generated by Django 3.2 on 2021-11-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='handle',
            field=models.TextField(blank=True, null=True),
        ),
    ]