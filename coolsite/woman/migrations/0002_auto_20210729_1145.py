# Generated by Django 3.2 on 2021-07-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woman', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ('id',), 'verbose_name': 'Известные женщины', 'verbose_name_plural': 'Известные женщины'},
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='women',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
