# Generated by Django 5.1.4 on 2024-12-25 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_grid_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grid",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
