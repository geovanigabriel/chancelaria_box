# Generated by Django 4.2.3 on 2023-08-11 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='arquidiocese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=9, null=True, unique=True, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=150, verbose_name='Localização')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Arquidiocese',
            },
        ),
        migrations.CreateModel(
            name='congregacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=9, null=True, unique=True, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=150, verbose_name='Localização')),
                ('fotoperfil', models.ImageField(upload_to='imf_perfil_congregacao', verbose_name='Foto de perfil')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Congregação',
            },
        ),
        migrations.CreateModel(
            name='diocese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Diocese')),
                ('telefone', models.CharField(blank=True, max_length=9, null=True, unique=True, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=150, verbose_name='Localização')),
                ('email', models.EmailField(max_length=254)),
                ('fotoperfil', models.ImageField(upload_to='img_perfil_diocese', verbose_name='Foto de perfil')),
                ('arquidiocesefk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chancelaria.arquidiocese', verbose_name='Arquidiocese')),
            ],
        ),
        migrations.CreateModel(
            name='livroBaptismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500, verbose_name='Descrição')),
                ('numero', models.CharField(max_length=4)),
                ('datainicio', models.DateField(verbose_name='Data do inicio')),
                ('datafim', models.DateField(verbose_name='Data do encerramento')),
                ('fotoperfil', models.ImageField(help_text='Imagem Para Capa do Livro', upload_to='imgagem_capa', verbose_name='Imagem de capa')),
                ('diocese', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.diocese', verbose_name='Diocese de proveniencia')),
            ],
            options={
                'verbose_name': 'Livro de registos do Baptismo',
            },
        ),
        migrations.CreateModel(
            name='paroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('telefone', models.CharField(blank=True, max_length=9, null=True, unique=True, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=150, verbose_name='Localização')),
                ('email', models.EmailField(max_length=254)),
                ('fotoperfil', models.ImageField(upload_to='img_perfil_paroquia', verbose_name='Foto de perfil')),
                ('congregacao', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.PROTECT, to='chancelaria.congregacao', verbose_name='Congreção tutelar')),
            ],
        ),
        migrations.CreateModel(
            name='provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Província',
            },
        ),
        migrations.CreateModel(
            name='zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('diocesefk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chancelaria.diocese', verbose_name='Diocese')),
            ],
        ),
        migrations.CreateModel(
            name='vigararia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=9, null=True, unique=True, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=150, verbose_name='Localização')),
                ('email', models.EmailField(max_length=254)),
                ('zona', models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.PROTECT, to='chancelaria.zona', verbose_name='Zona pastoral')),
            ],
        ),
        migrations.CreateModel(
            name='registoCasamento',
            fields=[
                ('nomenoivo', models.CharField(max_length=200, verbose_name='Nome Completo do noivo')),
                ('nascimentonoivo', models.DateField(verbose_name='Data de nascimento')),
                ('estadocivilnoivo', models.CharField(choices=[('Casado', 'Casado'), ('Soteiro(a)', 'solteiro(a)')], max_length=10, verbose_name='Estado Civil')),
                ('profissaonoivo', models.CharField(max_length=100, verbose_name='Profissão')),
                ('naturalidadenoivo', models.CharField(max_length=200, verbose_name='Natural')),
                ('nomepainoivo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome do Pai')),
                ('nomemaenoivo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome da Mãe')),
                ('nomenoiva', models.CharField(max_length=200, verbose_name='Nome Completo do noivo')),
                ('nascimentonoiva', models.DateField(verbose_name='Data de nascimento')),
                ('estadocivilnoiva', models.CharField(choices=[('Casado', 'Casado'), ('Soteiro(a)', 'solteiro(a)')], max_length=10, verbose_name='Estado Civil')),
                ('profissaonoiva', models.CharField(max_length=100, verbose_name='Profissão')),
                ('naturalidadenoiva', models.CharField(max_length=200, verbose_name='Natural')),
                ('nomepainoiva', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome do Pai')),
                ('nomemaenoiva', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome da Mãe')),
                ('numero', models.IntegerField(primary_key=True, serialize=False, verbose_name='Assento nº')),
                ('folha', models.IntegerField(verbose_name='Fl nº')),
                ('sobrenome', models.CharField(max_length=90, verbose_name='Apelido adoptado pelos nubentes')),
                ('celebrante', models.CharField(max_length=200, verbose_name='Celebrante')),
                ('municipio', models.CharField(max_length=200, verbose_name='Municipio')),
                ('imagemfrente', models.ImageField(upload_to='img_assento_casamento', verbose_name='Imagem Frente')),
                ('imagemverso', models.ImageField(upload_to='img_assento_casamento', verbose_name='Imagem Verso')),
                ('data', models.DateField(verbose_name='Data do matrimonio')),
                ('diocese', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chancelaria.diocese')),
                ('igreja', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.paroquia', verbose_name='Igreja')),
                ('provincianoiva', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='Provincia', to='chancelaria.provincia', verbose_name='Provincia')),
                ('provincianoivo', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.provincia', verbose_name='Provincia')),
            ],
            options={
                'verbose_name': 'Assentos de Casamento',
            },
        ),
        migrations.CreateModel(
            name='registoBaptismo',
            fields=[
                ('data', models.DateField(verbose_name='Data do Baptismo')),
                ('concelho', models.CharField(blank=True, max_length=100, null=True)),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=150, verbose_name='Sobrenome')),
                ('nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('numero', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Número do registo')),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=9)),
                ('municipio', models.CharField(blank=True, max_length=100, null=True)),
                ('distrito', models.CharField(blank=True, max_length=100, null=True)),
                ('hora', models.DateTimeField(auto_now_add=True, null=True)),
                ('raca', models.CharField(blank=True, choices=[('Negra', 'Negra'), ('Branca', 'Branca'), ('Mista', 'Mista')], max_length=7, null=True, verbose_name='Raça')),
                ('nomepai', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome do Pai')),
                ('resindeciapai', models.CharField(blank=True, max_length=150, null=True, verbose_name='Endereço do Pai')),
                ('estadocivilapai', models.CharField(blank=True, choices=[('Casado', 'Casado'), ('Soteiro(a)', 'solteiro(a)')], max_length=150, null=True, verbose_name='Estado civil do Pai')),
                ('naturalidadepai', models.CharField(blank=True, max_length=150, null=True, verbose_name='Naturalidade do Pai')),
                ('profissaopai', models.CharField(blank=True, max_length=150, null=True, verbose_name='Profissão do Pai')),
                ('nomemae', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome da Mãe')),
                ('estadocivilmae', models.CharField(blank=True, choices=[('Casado', 'Casado'), ('Soteiro(a)', 'solteiro(a)')], max_length=150, null=True, verbose_name='Estado civil da Mãe')),
                ('residenciamae', models.CharField(blank=True, max_length=150, null=True, verbose_name='Endereço da Mãe')),
                ('naturalidademae', models.CharField(blank=True, max_length=150, null=True, verbose_name='Naturalidade da Mãe')),
                ('profissaomae', models.CharField(blank=True, max_length=150, null=True, verbose_name='Profissão da Mãe')),
                ('netopaternohomem', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome do progenitor do pai')),
                ('netopaternomulher', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome da progenitora do pai')),
                ('netomaternohomem', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome do progenitor da mãe')),
                ('netomaternomulher', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome da progenitora do mãe')),
                ('padrinho', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome completo do Padrinho')),
                ('padrinholocalbaptismo', models.CharField(blank=True, max_length=150, null=True, verbose_name='local de baptismo do Padrinho')),
                ('padrinhoestadocivil', models.CharField(blank=True, choices=[('Casado', 'Casado'), ('Soteiro(a)', 'solteiro(a)')], max_length=15, null=True, verbose_name='Estado civil do Padrinho')),
                ('padrinhoprofissao', models.CharField(blank=True, choices=[('Casado', 'Casado'), ('Soteiro(a)', 'solteiro(a)')], max_length=15, null=True, verbose_name='Profissão do Padrinho')),
                ('madrinha', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome completo Madrinha')),
                ('madrinhalocalbaptismo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Local do baptismo da Madrinha')),
                ('madrinhaestadocivil', models.CharField(blank=True, choices=[('Casado', 'Casado'), ('Soteiro(a)', 'solteiro(a)')], max_length=150, null=True, verbose_name='Estado cilvil da Madrinha')),
                ('madrinhaprofissao', models.CharField(blank=True, choices=[('Casado', 'Casado'), ('Soteiro(a)', 'solteiro(a)')], max_length=150, null=True, verbose_name='Profissão da Madrinha')),
                ('imagem', models.ImageField(upload_to='img_baptismo', verbose_name='Imagem do assento')),
                ('diocese', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.diocese')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chancelaria.livrobaptismo')),
                ('naturalidade', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.provincia')),
                ('paroquia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chancelaria.paroquia')),
            ],
            options={
                'verbose_name_plural': 'Registo de Baptismo',
            },
        ),
        migrations.CreateModel(
            name='provinciaeclesiastica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('provincia', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.provincia')),
            ],
            options={
                'verbose_name_plural': 'Província Eclesiatisca',
            },
        ),
        migrations.AddField(
            model_name='paroquia',
            name='vigarariafk',
            field=models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.PROTECT, to='chancelaria.vigararia', verbose_name='Vigararia'),
        ),
        migrations.CreateModel(
            name='livroCasamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500, verbose_name='Descrição')),
                ('datainicio', models.DateField(help_text='formato da data: 2000-01-01', verbose_name='Data do inicio')),
                ('ano', models.IntegerField(unique_for_year='Registo do Ano')),
                ('datafim', models.DateField(verbose_name='Data do encerramento')),
                ('fotoperfil', models.ImageField(height_field=150, help_text='Imagem Para Capa do Livro', upload_to='imgagem_capa', verbose_name='Imagem de Capa', width_field=150)),
                ('diocese', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.diocese', verbose_name='Diocese de proveniencia')),
                ('paroquia', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.paroquia', verbose_name='Paróquia de proveniencia')),
                ('provincia', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.provincia', verbose_name='Província de proveniencia')),
            ],
            options={
                'verbose_name': 'Registos de Casamento',
            },
        ),
        migrations.AddField(
            model_name='livrobaptismo',
            name='paroquia',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.paroquia', verbose_name='Paroquia de Proveniencia'),
        ),
        migrations.AddField(
            model_name='livrobaptismo',
            name='provincia',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.provincia', verbose_name='Provincia de Proveniencia'),
        ),
        migrations.AddField(
            model_name='diocese',
            name='provincia',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='chancelaria.provincia', verbose_name='Provincia'),
        ),
        migrations.CreateModel(
            name='centro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('telefone', models.CharField(blank=True, max_length=9, null=True, unique=True, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=150, verbose_name='Localização')),
                ('email', models.EmailField(max_length=254)),
                ('fotoperfil', models.ImageField(upload_to='img_perfil_centro', verbose_name='Foto de perfil')),
                ('paroquiafk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chancelaria.paroquia', verbose_name='Paroquia')),
            ],
        ),
        migrations.AddField(
            model_name='arquidiocese',
            name='provinciaeclesiaciaticafk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chancelaria.provinciaeclesiastica', verbose_name='Província Eclesiatica'),
        ),
    ]
