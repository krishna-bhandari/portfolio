# Generated by Django 3.0.6 on 2020-07-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
