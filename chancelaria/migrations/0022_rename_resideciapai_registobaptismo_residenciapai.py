# Generated by Django 4.2.3 on 2023-08-13 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chancelaria', '0021_rename_residenciamae_registobaptismo_resideciamae'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registobaptismo',
            old_name='resideciapai',
            new_name='residenciapai',
        ),
    ]