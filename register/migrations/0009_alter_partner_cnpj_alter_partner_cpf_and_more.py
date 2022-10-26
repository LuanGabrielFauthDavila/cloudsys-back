# Generated by Django 4.1.1 on 2022-10-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_partner_company_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='cnpj',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='cpf',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='email',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='partner',
            name='fantasy_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='ie',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]