# Generated by Django 2.2.1 on 2019-06-29 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a_small_world', '0015_auto_20190623_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='catagories_id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='distributor_id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_manufacturer_id',
        ),
        migrations.AddField(
            model_name='products',
            name='catagories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='a_small_world.Catagories'),
        ),
        migrations.AddField(
            model_name='products',
            name='distributors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='a_small_world.Distributors'),
        ),
        migrations.AddField(
            model_name='products',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='a_small_world.Manufacturers'),
        ),
        migrations.AlterField(
            model_name='catagories',
            name='HH',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='catagories',
            name='MM',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='catagories',
            name='sub_catagory_1',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='catagories',
            name='sub_catagory_2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_city',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_contact_first_name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_contact_last_name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_contact_title',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_country',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_sells',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_state',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_website',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='manufacturer_zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price_value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_discription',
            field=models.TextField(max_length=200, null=True),
        ),
    ]