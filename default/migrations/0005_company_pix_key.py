# Generated by Django 4.1.1 on 2022-11-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0004_state_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='pix_key',
            field=models.CharField(blank=True, default='', max_length=19, null=True),
        ),
    ]