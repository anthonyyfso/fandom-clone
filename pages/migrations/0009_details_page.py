# Generated by Django 5.1 on 2024-08-31 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_remove_details_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='pages.pages'),
        ),
    ]
