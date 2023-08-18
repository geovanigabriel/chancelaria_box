from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
sexo = [('Masculino', 'Masculino'), ('Femenino', 'Femenino')]
congrega = [('Religiosa', 'Religiosa'), ('Diocesana', 'Diocesana')]
raca = [('Negra', 'Negra'), ('Branca', 'Branca'), ('Mista', 'Mista')]
estadocivil = [('Casado(a)', 'Casado(a)'), ('Soteiro(a)', 'solteiro(a)'), ('Viùvo(a)', 'Viùvo(a)'), ('Divorciado(a)', 'Divorciado(a)')]
################   ESTRUTURA DA IGREJA  #############

class provincia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, unique=True)
    class Meta:
        verbose_name_plural = 'Província'
    def __str__(self):
        return self.nome
class provinciaeclesiastica(models.Model):
    nome = models.CharField( max_length=100, null=False, blank=False)
    provincia = models.ForeignKey(provincia, max_length=100, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Província Eclesiatisca'
    def __str__(self):
        return self.nome
class arquidiocese(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, unique=True)
    provinciaeclesiaciaticafk = models.ForeignKey(provinciaeclesiastica, null=False, blank=False, verbose_name='Província Eclesiatica', on_delete=models.PROTECT)
    telefone = models.CharField(max_length=9, unique=True, null=True, blank=True, verbose_name='Telefone')
    endereco = models.CharField(max_length=150, null=False, blank=False, verbose_name='Localização')
    email = models.EmailField()
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name= 'Arquidiocese'
class congregacao(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=9, unique=True, null=True, blank=True, verbose_name='Telefone')
    endereco = models.CharField(max_length=150, null=False, blank=False, verbose_name='Localização')
    fotoperfil = models.FileField(verbose_name='Foto de perfil', upload_to= 'imf_perfil_congregacao')
    email = models.EmailField()

    class Meta:
        verbose_name = 'Congregação'
    def __str__(self):
        return self.nome
class diocese(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, verbose_name='Diocese', unique=True)
    arquidiocesefk = models.ForeignKey(arquidiocese, null=False, blank=False, verbose_name='Arquidiocese', on_delete=models.PROTECT)
    provincia = models.ForeignKey(provincia, max_length=100, null=False, blank=False, verbose_name='Provincia', on_delete=models.CASCADE)
    telefone = models.CharField(max_length=9, unique=True, null=True, blank=True, verbose_name='Telefone')
    endereco = models.CharField(max_length=150, null=False, blank=False, verbose_name='Localização')
    email = models.EmailField()
    fotoperfil = models.FileField(verbose_name='Foto de perfil', upload_to='img_perfil_diocese')
    def __str__(self):
        return self.nome
class zona(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    diocesefk = models.ForeignKey(diocese, null=False, blank=False, verbose_name='Diocese', on_delete=models.PROTECT)
    def __str__(self):
        return self.nome
class vigararia (models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False, unique=True)
    zona = models.ForeignKey(zona, max_length=150, null=False, blank=False, verbose_name='Zona pastoral', on_delete=models.PROTECT)
    telefone = models.CharField(max_length=9, unique=True, null=True, blank=True, verbose_name='Telefone')
    endereco = models.CharField(max_length=150, null=False, blank=False, verbose_name='Localização')
    email = models.EmailField()
    def __str__(self):
        return self.nome
class paroquia(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    vigarariafk = models.ForeignKey(vigararia, max_length=150, null=False, blank=False, verbose_name='Vigararia', on_delete=models.PROTECT)
    congregacao = models.ForeignKey(congregacao, null=False, blank=False, verbose_name='Congreção tutelar', max_length=100, on_delete=models.PROTECT)
    telefone = models.CharField(max_length=9, unique=True, null=True, blank=True, verbose_name='Telefone', default=' ')
    endereco = models.CharField(max_length=150, null=False, blank=False, verbose_name='Localização')
    email = models.EmailField()
    fotoperfil = models.FileField(verbose_name='Foto de perfil', upload_to ='img_perfil_paroquia')
    def __str__(self):
        return self.nome
class centro (models.Model):

    nome = models.CharField(max_length=150, null=False, blank=False)
    paroquiafk = models.ForeignKey(paroquia, null=False, blank=False, on_delete=models.PROTECT, verbose_name='Paroquia')
    telefone = models.CharField(max_length=9, unique=True, null=True, blank=True, verbose_name='Telefone')
    endereco = models.CharField(max_length=150, null=False, blank=False, verbose_name='Localização')
    email = models.EmailField()
    fotoperfil = models.FileField(verbose_name='Foto de perfil', upload_to='img_perfil_centro')
    def __str__(self):

        return self.nome

#########################     ARQUIVO  DA CHANCELARIA     ###################################

class livroCasamentoDuplicado(models.Model):
    nome = models.CharField(max_length=500, null=False, blank=False, verbose_name='Descrição')
    diocese = models.ForeignKey(diocese, null=False, blank=False, verbose_name='Diocese de proveniencia', on_delete=models.CASCADE, max_length=100)
    paroquia = models.ForeignKey(paroquia, null=False, blank=False, verbose_name='Paroquia de Proveniencia', on_delete=models.CASCADE, max_length=100)
    provincia = models.ForeignKey(provincia, null=False, blank=False, verbose_name='Provincia de Proveniencia', on_delete=models.CASCADE, max_length=100)
    datainicio = models.DateField(null=False, blank=False, verbose_name='Data do inicio', help_text='formato da data: 2000-01-01')
    datafim = models.DateField(null=False, blank=False, verbose_name='Data do encerramento')
    imagem = models.FileField(verbose_name='Imagem de capa', upload_to='imgagem_capa', help_text='Imagem Para Capa do Livro')
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Livro de Registos do Casamento'
class registoCasamento(models.Model):

    #################################   DADOS DO NOIVO      ########################################
    nomenoivo = models.CharField(max_length=200, null=False, blank=False, verbose_name='Nome Completo do noivo')
    nascimentonoivo = models.DateField(verbose_name='Data de nascimento')
    estadocivilnoivo = models.CharField(null=False, blank=False, choices=estadocivil, verbose_name='Estado Civil', max_length=14)
    profissaonoivo = models.CharField(null=False, blank=False, verbose_name='Profissão', max_length=100)
    naturalidadenoivo = models.CharField(null=False, blank=False, verbose_name='Natural', max_length=200)
    provincianoivo = models.ForeignKey(provincia, null=False, blank=False, verbose_name='Provincia', on_delete=models.CASCADE, max_length=50)
    nomepainoivo = models.CharField(verbose_name='Nome do Pai', max_length=200, null=True, blank=True, default='..........')
    nomemaenoivo = models.CharField(verbose_name='Nome da Mãe', max_length=200, null=True, blank=True, default='..........')

    #################################   DADOS DA NOIVA      ########################################

    nomenoiva = models.CharField(max_length=200, null=False, blank=False, verbose_name='Nome Completo do noivo')
    nascimentonoiva = models.DateField(verbose_name='Data de nascimento')
    estadocivilnoiva = models.CharField(null=False, blank=False, choices=estadocivil, verbose_name='Estado Civil', max_length=14)
    profissaonoiva = models.CharField(null=False, blank=False, verbose_name='Profissão', max_length=100)
    naturalidadenoiva = models.CharField(null=False, blank=False, verbose_name='Natural', max_length=200)
    provincianoiva = models.ForeignKey(provincia, null=False, blank=False, verbose_name='Provincia', on_delete=models.CASCADE, max_length=50, related_name='Provincia')
    nomepainoiva = models.CharField(verbose_name='Nome do Pai', max_length=200, null=True, blank=True, default='..........')
    nomemaenoiva = models.CharField(verbose_name='Nome da Mãe', max_length=200, null=True, blank=True, default='..........')

    ############################ DADOS DO ASSENTO ######################################################

    livro = models.ForeignKey(livroCasamentoDuplicado, max_length=100, null=False, blank=False,verbose_name='Livro', on_delete=models.DO_NOTHING)
    numero = models.IntegerField(primary_key=True, null=False, blank=False,verbose_name='Assento nº')
    folha = models.IntegerField(null=False, blank=False,verbose_name='Fl nº')
    sobrenome = models.CharField(max_length=90, null=False, blank=False, verbose_name='Apelido adoptado pelos nubentes')
    celebrante = models.CharField(max_length=200, null=False, blank=False, verbose_name='Celebrante')
    igreja = models.ForeignKey(paroquia, on_delete=models.CASCADE,max_length=200, null=False, blank=False, verbose_name='Igreja')
    municipio = models.CharField(max_length=200, null=False, blank=False, verbose_name='Municipio')
    diocese = models.ForeignKey(diocese, null=False, blank=False, on_delete=models.PROTECT)
    imagemfrente = models.FileField(null=False, blank=False, upload_to='img_assento_casamento', verbose_name='Imagem Frente')
    imagemverso = models.FileField(null=False, blank=False, upload_to='img_assento_casamento', verbose_name='Imagem Verso')
    data = models.DateField(null=False, blank=False, verbose_name='Data do matrimonio')

    class Meta:
        verbose_name = 'Assentos de Casamento'

    def __str__(self):
        return self.nomenoivo

class livroBaptismo(models.Model):
    nome = models.CharField(max_length=500, null=False, blank=False, verbose_name='Descrição')
    numero = models.CharField(max_length=4, blank=False, null=False)
    diocese = models.ForeignKey(diocese, null=False, blank=False, verbose_name='Diocese de proveniencia', on_delete=models.CASCADE, max_length=100)
    paroquia = models.ForeignKey(paroquia, null=False, blank=False, verbose_name='Paroquia de Proveniencia', on_delete=models.CASCADE, max_length=100)
    provincia = models.ForeignKey(provincia, null=False, blank=False, verbose_name='Provincia de Proveniencia', on_delete=models.CASCADE, max_length=100)
    datainicio = models.DateField(null=False, blank=False, verbose_name='Data do inicio')
    datafim = models.DateField(null=False, blank=False, verbose_name='Data do encerramento')
    imagem = models.FileField(verbose_name='Imagem de capa', upload_to='imgagem_capa', help_text='Imagem Para Capa do Livro')

    class Meta:
        verbose_name = 'Livro de Baptismo'

    def __str__(self):
        return self.nome
class registoBaptismo(models.Model):
    data = models.DateField(verbose_name='Data do Baptismo')
    concelho = models.CharField(blank=True, null=True, max_length=100)
    paroquia = models.ForeignKey(paroquia, blank=False, null=False, on_delete=models.PROTECT)
    nome = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nome')
    sobrenome = models.CharField(max_length=150, null=False, blank=False, verbose_name='Sobrenome')
    nascimento = models.DateField(verbose_name='Data de nascimento', blank=False, null=False)
    numero = models.CharField(max_length=4, null=False, blank=False, primary_key=True, verbose_name='Número do registo')
    folha = models.CharField(max_length=4, null=False, blank=False, unique=True, verbose_name='Fl')
    sexo = models.CharField(choices=sexo, max_length=9, null=False, blank=False)
    naturalidade = models.ForeignKey(provincia, null=False, blank=False, max_length=50, on_delete=models.CASCADE)
    municipio =  models.CharField(max_length=100, null=True, blank=True)
    distrito = models.CharField(max_length=100, blank=True, null=True)
    hora = models.DateTimeField(null=True, blank=True, )
    diocese = models.ForeignKey(diocese,max_length=100, blank=True, null=True, on_delete=models.CASCADE)
    livro = models.ForeignKey(livroBaptismo, null=False, blank=False, on_delete=models.CASCADE)
    raca = models.CharField(max_length=7, null=True, blank=True, choices=raca, verbose_name='Raça')
    nomepai = models.CharField(max_length=150,  verbose_name='Nome do Pai', null=True, blank=True)
    residenciapai = models.CharField(max_length=150,  verbose_name='Endereço do Pai', null=True, blank=True)
    estadocivilpai = models.CharField(choices=estadocivil, max_length=150,  verbose_name='Estado civil do Pai', null=True, blank=True)
    naturalidadepai = models.CharField(max_length=150,  verbose_name='Naturalidade do Pai', null=True, blank=True)
    profissaopai = models.CharField(max_length=150,  verbose_name='Profissão do Pai', null=True, blank=True)
    nomemae = models.CharField(max_length=150,  verbose_name='Nome da Mãe', null=True, blank=True)
    estadocivilmae = models.CharField(choices=estadocivil, max_length=150,  verbose_name='Estado civil da Mãe', null=True, blank=True)
    residenciamae = models.CharField(max_length=150,  verbose_name='Endereço da Mãe', null=True, blank=True)
    naturalidademae = models.CharField(max_length=150,  verbose_name='Naturalidade da Mãe', null=True, blank=True)
    profissaomae = models.CharField(max_length=150,  verbose_name='Profissão da Mãe', null=True, blank=True)
    netopaternohomem = models.CharField(max_length=150,  verbose_name='Nome do progenitor do pai', null=True, blank=True)
    netopaternomulher = models.CharField(max_length=150,  verbose_name='Nome da progenitora do pai',null=True, blank=True)
    netomaternohomem = models.CharField(max_length=150,  verbose_name='Nome do progenitor da mãe', null=True, blank=True)
    netomaternomulher = models.CharField(max_length=150,  verbose_name='Nome da progenitora do mãe', null=True, blank=True)
    padrinho = models.CharField(max_length=150, null=True, blank=True, verbose_name='Nome completo do Padrinho')
    padrinholocalbaptismo = models.CharField(max_length=150, null=True, blank=True, verbose_name='local de baptismo do Padrinho')
    padrinhoestadocivil = models.CharField(choices=estadocivil,max_length=15, null=True, blank=True, verbose_name='Estado civil do Padrinho')
    padrinhoprofissao = models.CharField(max_length=15, null=True, blank=False, verbose_name='Profissão do Padrinho')
    madrinha = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nome completo Madrinha')
    madrinhalocalbaptismo = models.CharField(max_length=150, null=False, blank=False, verbose_name='Local do baptismo da Madrinha')
    madrinhaestadocivil = models.CharField(choices=estadocivil, max_length=150, null=True, blank=True, verbose_name='Estado cilvil da Madrinha', default='..........')
    madrinhaprofissao = models.CharField(max_length=150, null=True, blank=True, verbose_name='Profissão da Madrinha', default='..........')
    imagem = models.FileField(verbose_name='Imagem do assento', upload_to='img_baptismo')

    class Meta:
        verbose_name_plural = 'Assento de Baptismo'

class pessoa(models.Model):
    from django_countries.fields import CountryField

    nome = models.CharField(max_length=200, null= True, blank=True, default=' ', help_text='Isso ajudará os seu amigos na pesquisa', verbose_name='Nome completo')
    pai = models.CharField(max_length=200, null= True, blank=True, default=' ', help_text='Esta campo fica pode ser util', verbose_name= 'Pai' )
    mae = models.CharField(max_length=200, null= True, blank=True, default=' ', help_text='Esta campo fica pode ser util', verbose_name='Mãe')
    bi = models.CharField(max_length=200, null= False, blank=False, primary_key=True, default=' ', help_text='Ela servirá como o seu identidicador')
    endereco = models.CharField(max_length=200, null= True, blank=True, default=' ', verbose_name='Endereço')
    provincia = models.ForeignKey(provincia, max_length=200, null= True, blank=True, default=' ', verbose_name='Província', on_delete=models.DO_NOTHING)
    nurural = models.CharField(max_length=200, null= True, blank=True, default=' ', verbose_name='Província, Cidade ou Estado')
    nascimento = models.DateField(verbose_name='Data de nascimento', name=False, blank=False, help_text='2000-01-01')
    sexo = models.CharField(choices=sexo, max_length=10, verbose_name='Sexo', null=False, blank=False)
    pais = CountryField(default='Angola', null=False, blank=False, verbose_name='Páis')
    nacionalidade = models.CharField(max_length=10, verbose_name='Nacionalidade', null=False, blank=False, default='Angolana')
    estadocivil = models.CharField(choices=estadocivil, verbose_name='Estado civil', max_length=14)
