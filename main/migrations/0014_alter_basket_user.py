# Generated by Django 4.0.3 on 2022-04-24 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_basket_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]