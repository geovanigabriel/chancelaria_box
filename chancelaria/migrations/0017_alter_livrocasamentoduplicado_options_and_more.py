# Generated by Django 4.2.3 on 2023-08-13 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chancelaria', '0016_alter_registocasamento_livro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livrocasamentoduplicado',
            options={'verbose_name': 'Livro de Registos do Casamento'},
        ),
        migrations.DeleteModel(
            name='DuplicadosCasamento',
        ),
    ]