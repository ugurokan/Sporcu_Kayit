# Generated by Django 4.1.7 on 2023-05-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sporcu',
            name='Antrenorler',
            field=models.ManyToManyField(to='core.antrenor'),
        ),
        migrations.AlterField(
            model_name='antrenor',
            name='Branslar',
            field=models.ManyToManyField(to='core.brans'),
        ),
    ]
