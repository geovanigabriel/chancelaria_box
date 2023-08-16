# Generated by Django 4.2.3 on 2023-08-14 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chancelaria', '0023_rename_resideciamae_registobaptismo_residenciamae'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livrobaptismo',
            options={'verbose_name': 'Livro de Baptismo'},
        ),
        migrations.AlterModelOptions(
            name='registobaptismo',
            options={'verbose_name_plural': 'Assento de Baptismo'},
        ),
        migrations.RenameField(
            model_name='registocasamento',
            old_name='Livro',
            new_name='livro',
        ),
        migrations.AlterField(
            model_name='registobaptismo',
            name='hora',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]