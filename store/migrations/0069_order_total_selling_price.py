# Generated by Django 4.2.7 on 2023-12-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0068_remove_orderitem_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_selling_price',
            field=models.IntegerField(default=0),
        ),
    ]
