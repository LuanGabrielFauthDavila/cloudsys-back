# Generated by Django 4.1.1 on 2022-10-25 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_alter_partner_person_f_j'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='fantasy_name',
            new_name='fantasy',
        ),
    ]