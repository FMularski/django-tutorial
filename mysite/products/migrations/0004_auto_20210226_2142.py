# Generated by Django 3.1.7 on 2021-02-26 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('products', '0003_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
