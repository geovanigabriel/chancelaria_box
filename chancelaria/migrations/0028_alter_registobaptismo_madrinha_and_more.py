# Generated by Django 4.2.3 on 2023-08-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chancelaria', '0027_alter_centro_fotoperfil_alter_congregacao_fotoperfil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registobaptismo',
            name='madrinha',
            field=models.CharField(default=122, max_length=150, verbose_name='Nome completo Madrinha'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registobaptismo',
            name='madrinhaestadocivil',
            field=models.CharField(blank=True, choices=[('Casado(a)', 'Casado(a)'), ('Soteiro(a)', 'solteiro(a)'), ('Viùvo(a)', 'Viùvo(a)'), ('Divorciado(a)', 'Divorciado(a)')], default='..........', max_length=150, null=True, verbose_name='Estado cilvil da Madrinha'),
        ),
        migrations.AlterField(
            model_name='registobaptismo',
            name='madrinhalocalbaptismo',
            field=models.CharField(max_length=150, verbose_name='Local do baptismo da Madrinha'),
        ),
        migrations.AlterField(
            model_name='registobaptismo',
            name='madrinhaprofissao',
            field=models.CharField(blank=True, default='..........', max_length=150, null=True, verbose_name='Profissão da Madrinha'),
        ),
        migrations.AlterField(
            model_name='registobaptismo',
            name='padrinhoprofissao',
            field=models.CharField(max_length=15, null=True, verbose_name='Profissão do Padrinho'),
        ),
        migrations.AlterField(
            model_name='registocasamento',
            name='nomemaenoiva',
            field=models.CharField(blank=True, default='..........', max_length=200, null=True, verbose_name='Nome da Mãe'),
        ),
        migrations.AlterField(
            model_name='registocasamento',
            name='nomemaenoivo',
            field=models.CharField(blank=True, default='..........', max_length=200, null=True, verbose_name='Nome da Mãe'),
        ),
        migrations.AlterField(
            model_name='registocasamento',
            name='nomepainoiva',
            field=models.CharField(blank=True, default='..........', max_length=200, null=True, verbose_name='Nome do Pai'),
        ),
        migrations.AlterField(
            model_name='registocasamento',
            name='nomepainoivo',
            field=models.CharField(blank=True, default='..........', max_length=200, null=True, verbose_name='Nome do Pai'),
        ),
    ]