# Generated by Django 4.2.3 on 2023-07-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chancelaria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livrobaptismo',
            name='nome',
            field=models.CharField(default=111, max_length=500, verbose_name='Descrição'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livrocasamento',
            name='nome',
            field=models.CharField(default=111, max_length=500, verbose_name='Descrição'),
            preserve_default=False,
        ),
    ]