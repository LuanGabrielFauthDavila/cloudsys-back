# Generated by Django 4.1.4 on 2022-12-29 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_sale_canceled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
