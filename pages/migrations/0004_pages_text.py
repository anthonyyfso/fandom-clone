# Generated by Django 5.1 on 2024-08-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_delete_heading_remove_pages_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='text',
            field=models.CharField(default='Default content', max_length=100000),
        ),
    ]
