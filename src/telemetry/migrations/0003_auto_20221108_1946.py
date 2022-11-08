# Generated by Django 3.2.8 on 2022-11-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemetry', '0002_auto_20221107_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagvalue',
            name='created',
        ),
        migrations.AddField(
            model_name='tagvalue',
            name='timestamp',
            field=models.DateTimeField(null=True, verbose_name='timestamp'),
        ),
        migrations.AddField(
            model_name='tagvalue',
            name='version',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='version'),
        ),
    ]