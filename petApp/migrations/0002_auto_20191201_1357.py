# Generated by Django 2.2.7 on 2019-12-01 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='kind',
            field=models.CharField(choices=[('C', 'Cat'), ('D', 'Dog')], default='Dog', max_length=1),
        ),
    ]
