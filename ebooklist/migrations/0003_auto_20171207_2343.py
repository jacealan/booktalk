# Generated by Django 2.0 on 2017-12-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebooklist', '0002_auto_20171207_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeid',
            name='aladin_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='storeid',
            name='ridibooks_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='storeid',
            name='yes24_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
