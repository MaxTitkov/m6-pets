# Generated by Django 2.2.7 on 2019-12-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petApp', '0002_auto_20191201_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='city',
            field=models.CharField(default='Москва', max_length=50),
            preserve_default=False,
        ),
    ]
