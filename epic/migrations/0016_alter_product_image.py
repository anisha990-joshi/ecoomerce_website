# Generated by Django 3.2.9 on 2021-11-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epic', '0015_auto_20211120_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, db_column='Image', null=True, upload_to='epic/images/'),
        ),
    ]
