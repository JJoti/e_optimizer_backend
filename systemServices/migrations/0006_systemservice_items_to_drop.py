# Generated by Django 4.2 on 2024-07-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemServices', '0005_systemservice_list_css_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemservice',
            name='items_to_drop',
            field=models.IntegerField(default=2),
        ),
    ]
