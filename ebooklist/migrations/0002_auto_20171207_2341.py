# Generated by Django 2.0 on 2017-12-07 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebooklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeid',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='storeid',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
