# Generated by Django 4.2.3 on 2023-08-19 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chancelaria', '0032_alter_registobaptismo_municipio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registobaptismo',
            name='distrito',
            field=models.CharField(blank=True, default='..........', max_length=100, null=True),
        ),
    ]
