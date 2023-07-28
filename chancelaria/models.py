from django.db import models

# Create your models here.
sexo = [('Masculino', 'Masculino'), ('Femenino', 'Femenino')]
congrega = [('Religiosa', 'Religiosa'), ('Diocesana', 'Diocesana')]
raca = [('Negra', 'Negra'), ('Branca', 'Branca'), ('Mista', 'Mista')]
estadocivil = [('Casado', 'Casado'), ('Soteiro(a)', 'solteiro(a)')]
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
    fotoperfil = models.ImageField(verbose_name='Foto de perfil', upload_to= 'imf_perfil_congregacao')
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
    fotoperfil = models.ImageField(verbose_name='Foto de perfil', upload_to='img_perfil_diocese')
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
    telefone = models.CharField(max_length=9, unique=True, null=True, blank=True, verbose_name='Telefone')
    endereco = models.CharField(max_length=150, null=False, blank=False, verbose_name='Localização')
    email = models.EmailField()
    fotoperfil = models.ImageField(verbose_name='Foto de perfil', upload_to ='img_perfil_paroquia')
    def __str__(self):
        return self.nome
class centro (models.Model):

    nome = models.CharField(max_length=150, null=False, blank=False)
    paroquiafk = models.ForeignKey(paroquia, null=False, blank=False, on_delete=models.PROTECT, verbose_name='Paroquia')
    telefone = models.CharField(max_length=9, unique=True, null=True, blank=True, verbose_name='Telefone')
    endereco = models.CharField(max_length=150, null=False, blank=False, verbose_name='Localização')
    email = models.EmailField()
    fotoperfil = models.ImageField(verbose_name='Foto de perfil', upload_to='img_perfil_centro')
    def __str__(self):

        return self.nome

#########################     ARQUIVO  DA CHANCELARIA     ###################################
class livroCasamento(models.Model):
    nome = models.CharField(max_length=500, null=False, blank=False, verbose_name='Descrição')
    diocese = models.ForeignKey(diocese, null=False, blank=False, verbose_name='Diocese de proveniencia', on_delete=models.CASCADE, max_length=100)
    paroquia = models.ForeignKey(paroquia, null=False, blank=False, verbose_name='Paróquia de proveniencia', on_delete=models.CASCADE, max_length=100)
    provincia = models.ForeignKey(provincia, null=False, blank=False, verbose_name='Província de proveniencia', on_delete=models.CASCADE, max_length=100)
    datainicio = models.DateField(null=False, blank=False, verbose_name='Data do inicio', help_text='formato da data: 2000-01-01')
    ano = models.IntegerField(unique_for_year='Registo do Ano')
    datafim = models.DateField(null=False, blank=False, verbose_name='Data do encerramento')
    fotoperfil = models.ImageField(width_field=150, height_field=150, verbose_name='Imagem de Capa', upload_to='imgagem_capa', help_text='Imagem Para Capa do Livro')

    class Meta:
        verbose_name = 'Registos de Casamento'
class registoCasamento(models.Model):

    #################################   DADOS DO NOIVO      ########################################
    nomenoivo = models.CharField(max_length=200, null=False, blank=False, verbose_name='Nome Completo do noivo')
    nascimentonoivo = models.DateField(verbose_name='Data de nascimento')
    estadocivilnoivo = models.CharField(null=False, blank=False, choices=estadocivil, verbose_name='Estado Civil', max_length=10)
    profissaonoivo = models.CharField(null=False, blank=False, verbose_name='Profissão', max_length=100)
    naturalidadenoivo = models.CharField(null=False, blank=False, verbose_name='Natural', max_length=200)
    provincianoivo = models.ForeignKey(provincia, null=False, blank=False, verbose_name='Provincia', on_delete=models.CASCADE, max_length=50)
    nomepainoivo = models.CharField(verbose_name='Nome do Pai', max_length=200, null=True, blank=True)
    nomemaenoivo = models.CharField(verbose_name='Nome da Mãe', max_length=200, null=True, blank=True)

    #################################   DADOS DA NOIVA      ########################################

    nomenoiva = models.CharField(max_length=200, null=False, blank=False, verbose_name='Nome Completo do noivo')
    nascimentonoiva = models.DateField(verbose_name='Data de nascimento')
    estadocivilnoiva = models.CharField(null=False, blank=False, choices=estadocivil, verbose_name='Estado Civil', max_length=10)
    profissaonoiva = models.CharField(null=False, blank=False, verbose_name='Profissão', max_length=100)
    naturalidadenoiva = models.CharField(null=False, blank=False, verbose_name='Natural', max_length=200)
    provincianoiva = models.ForeignKey(provincia, null=False, blank=False, verbose_name='Provincia', on_delete=models.CASCADE, max_length=50, related_name='Provincia')
    nomepainoiva = models.CharField(verbose_name='Nome do Pai', max_length=200, null=True, blank=True)
    nomemaenoiva = models.CharField(verbose_name='Nome da Mãe', max_length=200, null=True, blank=True)

    ############################ DADOS DO ASSENTO ######################################################

    numero = models.IntegerField(primary_key=True, null=False, blank=False,verbose_name='Assento nº')
    folha = models.IntegerField(null=False, blank=False,verbose_name='Fl nº')
    sobrenome = models.CharField(max_length=90, null=False, blank=False, verbose_name='Apelido adoptado pelos nubentes')
    celebrante = models.CharField(max_length=200, null=False, blank=False, verbose_name='Celebrante')
    igreja = models.ForeignKey(paroquia, on_delete=models.CASCADE,max_length=200, null=False, blank=False, verbose_name='Igreja')
    municipio = models.CharField(max_length=200, null=False, blank=False, verbose_name='Municipio')
    diocese = models.ForeignKey(diocese, null=False, blank=False, on_delete=models.PROTECT)
    imagemfrente = models.ImageField(null=False, blank=False, upload_to='img_assento_casamento', verbose_name='Imagem Frente')
    imagemverso = models.ImageField(null=False, blank=False, upload_to='img_assento_casamento', verbose_name='Imagem Verso')
    data = models.DateField(null=False, blank=False, verbose_name='Data do matrimonio')

    class Meta:
        verbose_name = 'Assentos de Casamento'

    def __str__(self):
        return self.nomenoivo

class livroBaptismo(models.Model):
    nome = models.CharField(max_length=500, null=False, blank=False, verbose_name='Descrição')
    numero = models.CharField(max_length=4, blank=False, null=False)
    diocese = models.ForeignKey(diocese, null=False, blank=False, verbose_name='Diocese de proveniencia', on_delete=models.CASCADE, max_length=100)
    paroquia = models.ForeignKey(paroquia, null=False, blank=False, verbose_name='Diocese de proveniencia', on_delete=models.CASCADE, max_length=100)
    provincia = models.ForeignKey(provincia, null=False, blank=False, verbose_name='Diocese de província', on_delete=models.CASCADE, max_length=100)
    datainicio = models.DateField(null=False, blank=False, verbose_name='Data do inicio')
    datafim = models.DateField(null=False, blank=False, verbose_name='Data do encerramento')
    fotoperfil = models.ImageField(verbose_name='Imagem de capa', upload_to='imgagem_capa', help_text='Imagem Para Capa do Livro')

    class Meta:
        verbose_name = 'Livro de registos do Baptismo'

    def __str__(self):
        return self.numero

class registoBaptismo(models.Model):
    data = models.DateField(verbose_name='Data do Baptismo')
    concelho = models.CharField(blank=True, null=True, max_length=100)
    paroquia = models.ForeignKey(paroquia, blank=False, null=False, on_delete=models.PROTECT)
    nome = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nome')
    sobrenome = models.CharField(max_length=150, null=False, blank=False, verbose_name='Sobrenome')
    nascimento = models.DateField(verbose_name='Data de nascimento', blank=False, null=False)
    numero = models.CharField(max_length=4, null=False, blank=False, primary_key=True, verbose_name='Número do registo')
    sexo = models.CharField(choices=sexo, max_length=9, null=False, blank=False)
    naturalidade = models.ForeignKey(provincia, null=False, blank=False, max_length=50, on_delete=models.CASCADE)
    livro = models.ForeignKey(livroBaptismo, null=False, blank=False, on_delete=models.CASCADE)
    raca = models.CharField(max_length=7, null=True, blank=True, choices=raca, verbose_name='Raça')
    nomepai = models.CharField(max_length=150,  verbose_name='Nome do Pai', null=True, blank=True)
    nomemae = models.CharField(max_length=150,  verbose_name='Nome da Mãe', null=True, blank=True)
    netopaternohomem = models.CharField(max_length=150,  verbose_name='Nome do progenitor do pai', null=True, blank=True)
    netopaternomulher = models.CharField(max_length=150,  verbose_name='Nome da progenitora do pai',null=True, blank=True)
    netomaternohomem = models.CharField(max_length=150,  verbose_name='Nome do progenitor da mãe', null=True, blank=True)
    netomaternomulher = models.CharField(max_length=150,  verbose_name='Nome da progenitora do mãe', null=True, blank=True)
    padrinho = models.CharField(max_length=150, null=True, blank=True, verbose_name='Padrinho')
    madrinha = models.CharField(max_length=150, null=True, blank=True, verbose_name='Madrinha')
    imagem = models.ImageField(verbose_name='Imagem do assento', upload_to='img_baptismo')

    class Meta:
        verbose_name_plural = 'Registo de Baptismo'