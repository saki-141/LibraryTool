# Generated by Django 2.1.5 on 2019-06-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_auto_20190612_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tag2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='tag3',
            field=models.CharField(blank=True, default=0, max_length=100),
            preserve_default=False,
        ),
    ]
