# Generated by Django 4.1.4 on 2022-12-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(choices=[('film', 'Film'), ('home', 'Home'), ('clothes', 'Clothes'), ('health', 'Health'), ('electronic', 'Electronic'), ('misc', 'Misc')], default='misc', max_length=25),
        ),
    ]
