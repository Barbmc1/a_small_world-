# Generated by Django 2.2.1 on 2019-06-06 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_small_world', '0005_auto_20190606_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagories',
            name='sub_catagory_2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=50),
        ),
    ]