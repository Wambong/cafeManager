# Generated by Django 5.1.6 on 2025-06-02 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_customerorder_country_customerorder_state"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="stock",
            field=models.PositiveIntegerField(default=10, help_text="Available stock"),
        ),
    ]
