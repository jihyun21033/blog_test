# Generated by Django 3.0.4 on 2020-03-11 20:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_infodata'),
    ]

    operations = [
        migrations.AddField(
            model_name='infodata',
            name='login_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
