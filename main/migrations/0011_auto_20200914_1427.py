# Generated by Django 3.1.1 on 2020-09-14 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_order_order_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_notes',
        ),
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=510, null=True),
        ),
    ]