# Generated by Django 4.2.3 on 2023-08-12 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chancelaria', '0008_alter_livrobaptismo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livrobaptismo',
            options={'verbose_name': 'Livro de registos do Baptismo'},
        ),
        migrations.CreateModel(
            name='livroCasamentoDuplicado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500, verbose_name='Descrição')),
                ('numero', models.CharField(max_length=4)),
                ('datainicio', models.DateField(verbose_name='Data do inicio')),
                ('datafim', models.DateField(verbose_name='Data do encerramento')),
                ('imagem', models.ImageField(help_text='Imagem Para Capa do Livro', upload_to='imgagem_capa', verbose_name='Imagem de capa')),
                ('diocese', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.diocese', verbose_name='Diocese de proveniencia')),
                ('paroquia', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.paroquia', verbose_name='Paroquia de Proveniencia')),
                ('provincia', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.provincia', verbose_name='Provincia de Proveniencia')),
            ],
            options={
                'verbose_name': 'Livro de registos do Casamento',
            },
        ),
    ]