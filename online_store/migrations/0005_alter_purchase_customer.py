# Generated by Django 4.0.2 on 2022-02-13 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('online_store', '0004_alter_purchase_date_of_purchase_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
