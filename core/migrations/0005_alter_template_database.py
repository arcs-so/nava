# Generated by Django 4.2.11 on 2024-06-16 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_database_connection_string_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='database',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.database'),
        ),
    ]