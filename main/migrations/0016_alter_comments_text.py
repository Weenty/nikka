# Generated by Django 4.0.3 on 2022-04-27 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_basket_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
