# Generated by Django 2.2.1 on 2019-06-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_small_world', '0004_auto_20190606_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagories',
            name='catagory_1',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='catagories',
            name='sub_catagory_1',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='catagories',
            name='sub_catagory_2',
            field=models.CharField(max_length=35),
        ),
    ]