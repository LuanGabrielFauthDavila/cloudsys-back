# Generated by Django 4.1.1 on 2022-10-25 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_remove_partner_person_type_partner_type_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='person_f_j',
            field=models.BooleanField(default=False),
        ),
    ]