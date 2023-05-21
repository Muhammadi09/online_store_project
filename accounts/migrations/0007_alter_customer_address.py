# Generated by Django 4.1.7 on 2023-03-21 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_customer_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.address'),
        ),
    ]
