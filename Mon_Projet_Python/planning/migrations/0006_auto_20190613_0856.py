# Generated by Django 2.2.2 on 2019-06-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0005_auto_20190613_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]