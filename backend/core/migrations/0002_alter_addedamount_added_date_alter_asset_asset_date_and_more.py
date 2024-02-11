# Generated by Django 5.0.2 on 2024-02-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addedamount',
            name='added_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='income_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='liability',
            name='liability_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='target',
            name='target_completion_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='target',
            name='target_set_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
