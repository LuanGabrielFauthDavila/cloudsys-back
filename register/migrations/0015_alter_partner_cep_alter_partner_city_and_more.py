# Generated by Django 4.0.4 on 2022-10-30 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0004_state_country'),
        ('register', '0014_partner_rg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='cep',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='city',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.PROTECT, to='default.city'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='district',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='num',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='street',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]