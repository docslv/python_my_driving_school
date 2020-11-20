# Generated by Django 2.2.2 on 2019-06-14 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planning', '0034_planning'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forfait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_forfait', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]