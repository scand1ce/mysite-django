# Generated by Django 3.0.4 on 2020-06-13 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200612_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=150, verbose_name='Название категории'),
        ),
    ]
