import datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import qrcode
from chancelaria.form import BaptimoForm, ParoquiaForm, centroForm, VigarariaForm, ArquidioceseForm, ProvinciaForm, \
    CongregacaoForm, ZonaForm, obitoForm, DioceseForm, LivroFormBaptismo, camentoForm, LivroFormCasamento, pessoaForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponse, FileResponse
from chancelaria.models import paroquia, provincia, provinciaeclesiastica, registoBaptismo, registoCasamento, \
    livroBaptismo, diocese, congregacao, zona, vigararia, arquidiocese, centro, \
    livroCasamentoDuplicado, pessoa
from fpdf import FPDF
from chancelaria.filters import dioceseBusca, paroquiaBusca, baptismoBusca, casamentoBusca, centroBusca
from io import BytesIO
from datetime import date

def assentoDeObito(request):
    form = obitoForm(request.POST)
    if form.is_valid():
        form.save()
    context = {'formulario':form}
    return render(request, 'obito.html', context)





def ver_livro(request, pk):

    registos = registoCasamento.objects.filter(pk)

    context = {'registo':registos, 'livro':registos}

    return render(request, 'livros.html', context)

































def ListaLivroCasamento(request):
    livros = livroCasamentoDuplicado.objects.all()
    return render(request, 'duplicadoscasamento.html', {'livros':livros})

@login_required()
def dioceselista(request):
    diocesebanco = diocese.objects.all()
    busca = dioceseBusca(request.GET, queryset=diocesebanco)
    context = {'diocese': diocesebanco, 'busca': busca}

    return render(request, 'listagem.html', context)

@login_required()
def livro_baptismo(request):
    banco = livroBaptismo.objects.all()
    context = {'livros': banco}
    return render(request, 'duplicados.html', context)


#################################      PERFIL      #####################################################
def perfil(request):
    banco = pessoa.objects.all()
    context = {'pessoa': banco}
    return render(request, 'perfil.html', context)

def preencherPerfil(request):
    form = pessoaForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect(home)
    context = {'pessoa': form}
    return render(request, 'preencherperfil.html', context)



#################################   UPDATES    #########################################################################

@login_required()
def updateCasamento(request, pk):
    banco = registoCasamento.objects.get(pk=pk)
    formulario = camentoForm(instance=banco)
    if formulario.is_valid():
        formulario.save()
        return redirect(home)
    context = {'formulario':formulario}
    return render(request, 'casamento.html', context)
def updateBaptismo(request, pk):
    banco = registoBaptismo.objects.get(pk=pk)
    formulario = BaptimoForm(request.POST or None, instance=banco)
    if formulario.is_valid():
        formulario.save()
        return redirect(home)
    context = {
        'formulario': formulario,
        'registo': banco
    }
    return render(request, 'baptismo.html', context)




@login_required()
def casamentoPesquisa(request):
    banco = registoCasamento.objects.all()
    busca = casamentoBusca(request.GET, queryset=banco)
    context = {
        'banco': banco,
        'busca': busca
    }
    return render(request, 'casamentobusca.html', context)

#####################    REGISTO DE ASSENTO  ####################

@login_required(login_url='account_login')
def registocasamento(request):
    formulario = camentoForm(request.POST, request.FILES)
    if formulario.is_valid():
        formulario.save()
        return redirect(casamentoPesquisa)
    context = {
        'formulario': formulario
    }

    return render(request, 'casamento.html', context)

#############################   CADASTRO DAS INSTITUIÇÕES #########################
@login_required()
def baptismocaCadastro(request):
    formulario = BaptimoForm(request.POST, request.FILES)
    if formulario.is_valid():
        formulario.save()
        return redirect(home)
    context = {
        'formulario': formulario
    }
    return render(request, 'baptismo.html', context)

#################### CADASTRO DE INSTITUIÇÕES    ######################
@login_required()
def paroquiaCadastro(request):
    formulario = ParoquiaForm(request.POST,  request.FILES)
    if formulario.is_valid():
        formulario.save()
        return redirect(home)
    context = {
        'formulario': formulario
    }
    return render(request, 'paroquia.html', context)

@login_required()
def centroCadastro(request):
        formulario = centroForm(request.POST, request.FILES )
        if formulario.is_valid():
            formulario.save()
            return redirect(home)
        context = {

            'formulario': formulario
        }
        return render(request, 'centro.html', context)

@login_required()
def vigarariaCadastro(request):
        formulario = VigarariaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(home)
        context = {

            'formulario': formulario
        }
        return render(request, 'vigararia.html', context)






@login_required()
def arquidioceseCadastro(request):

    formulario = ArquidioceseForm(request.POST , request.FILES )
    if formulario.is_valid():
        formulario.save()
        return redirect(home)
    context = {

    'formulario': formulario
        }
    return render(request, 'arquidiocese.html', context)

@login_required()
def congregacaoCadastro(request):

    formulario = CongregacaoForm(request.POST, request.FILES )
    if formulario.is_valid():
        formulario.save()
        return redirect(home)
    context = {

        'formulario': formulario
        }
    return render(request, 'congregacao.html', context)

@login_required()
def CadastrolivroCasamento(request):
    livroCasamento = LivroFormCasamento(request.POST)
    livroBaptismo = LivroFormBaptismo(request.POST)

    context = {
        'formulariocasamento': livroCasamento,
        'formulario': livroBaptismo

    }
    return render(request, 'livro.html', context)

@login_required()
def livrobaptismo(request):

    livroBaptismo = LivroFormBaptismo(request.POST)

    context = {
        'formulariobaptismo': livroBaptismo,
    }
    return render(request, 'livro.html', context)


@login_required()
def CadastroVigararia(request):
    vigararia = VigarariaForm(request.POST)
    if vigararia.is_valid():
        vigararia.save()
        return redirect(home)
    contexto = {
        'formulario':vigararia
    }
    return render(request, 'cadastrar.html', contexto)

@login_required()
def CadastroDiocese(request):
    diocese = DioceseForm(request.POST)
    if diocese.is_valid():
        diocese.save()
        return redirect(home)
    contexto = {
        'formulario': diocese
    }
    return render(request, 'cadastrar.html', contexto)

@login_required()
def CadastroZona(request):
    zona = ZonaForm(request.POST)

    if zona.is_valid():
        zona.save()
    conxteto = {
        'formulario':zona
    }

    return render(request, 'cadastrar.html', conxteto)

@login_required()
def listagemArquidiocese(request):
    banco = arquidiocese.objects.all()
    context = {
        'banco': banco
    }
    return render(request, 'listagem.html', context)



@login_required()
def listagemParoquia(request):
    banco = paroquia.objects.all()
    context = {
        'banco': banco
    }
    return render(request, 'listagem.html', context)

@login_required()
def listagemVigararia(request):
    banco = vigararia.objects.all()
    context = {
        'banco': banco
    }
    return render(request, 'listagem.html', context)

@login_required()
def listagemZona(request):
    banco = zona.objects.all()
    context = {
        'banco': banco
    }
    return render(request, 'listagem.html', context)



@login_required()
def listagemCongregacao(request):
    banco = congregacao.objects.all()
    context = {
        'banco': banco
    }
    return render(request, 'listagem.html', context)

@login_required()
def listagemProvinciaEclesiastica(request):
    banco = provinciaeclesiastica.objects.all()
    context = {
        'banco': banco
    }
    return render(request, 'listagem.html', context)


@login_required()
def delete(request, pk):
    pass

def dashebord(request):

    return render(request,'charts.html')


import cloudinary

cloudinary.config(
    cloud_name="dhhtynyan",
    api_key="685519654522669",
    api_secret="***************************"
)

#cloudinary.uploader.upload("https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg",
 # public_id = "olympic_flag")

@login_required()
def home(request):
    livros = livroBaptismo.objects.all()
    return render(request, 'home.html')

@login_required()
def CadastroParoquia(request):
    paroquia = ParoquiaForm(request.POST)
    if paroquia.is_valid():
        paroquia.save()
        return redirect(home)
    contexto = {
        'formulario': paroquia
    }
    return render(request, 'paroquia.html', contexto)




##########################   PESQUISA     #####################
@login_required()
def baptismoPesquisa(request):
    banco = registoBaptismo.objects.all()
    bancoprovincia = provincia.objects.all()
    busca = baptismoBusca(request.GET, queryset=banco)
    context = {'banco': banco,
               'busca': busca,
               'provincia': bancoprovincia
               }
    return render(request, 'baptismobusca.html', context)


mes = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
       'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

############################     P D F  BAPTISMO      #########################################
def baptismo_pdf(request, pk):
    from num2words import num2words
    baptismo = get_object_or_404(registoBaptismo, pk=pk)
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.set_fill_color(0, 0, 0) #cor das celulas
    ###################################################     CABEÇALHO ####################################
    pdf.image("chancelaria/templates/verdade.jpeg", 1, 40, 210, 295)
    pdf.image("./chancelaria/verdadebeleza.jpeg", 84, 0, 50, 55)
    #pdf.image(baptismo.imagem, 48, 23, 50, 44)
    validacaoQRCODE = qrcode.make(f'qrcode_de_validação_de Assentto de baptismo de {baptismo.nome}, '
                                  f'numero de registo {baptismo.numero}, registado na folha nº {baptismo.folha}')
    validacaoQRCODE.save(f'Assento_casamento.png')
    pdf.image('Assento_casamento.png', 84, 245, 35, 35)


    pdf.cell(10, 30, '                                                           ', 0 , 1 , 'C',  0, 'False')
    pdf.cell(180, 7, '                 ARQUIDIOCESE DE LUANDA', 0 , 1 , 'C',  0, 'False')
    pdf.cell(180, 5, '                CHANCELARIA ARQUIDIOCESANA', 0 , 1 , 'C',  0, 'False')
    pdf.cell(180, 10, '                  ASSENTO DE BAPTISMO DIGITAL', 0 , 1 , 'C',  0, 'False')
    pdf.cell(180, 10, '                  ', 0 , 1 , 'C',  0, 'False')
    pdf.cell(180, 8, '                 ====== CÚRIA ARQUIDIOCESANA ======', 0 , 1 , 'C',  0, 'False')

    ################################################## CONVERSÃO DA DATA POR EXTENSO ####################################
    datadia = baptismo.data.day ####   DIA VALOR NUMERICO
    dia = num2words(datadia, lang='pt-br') #### DIA POR EXTENSO
    datames = baptismo.data.month  #### MES VALOR NUMERICO
    dataano = baptismo.data.year ### ANO VALOR NUMERICO
    ano = num2words(dataano, lang='pt-br')  ### ANO POR EXTENSO

    dia_nascimento = baptismo.nascimento.day
    dianascimento = num2words(dia_nascimento, lang='pt-br')
    mes_nascimento = baptismo.nascimento.month
    mesnascimento = num2words(mes_nascimento, lang='pt-br')
    ano_nascimento = baptismo.nascimento.year
    anonascimento = num2words(ano_nascimento, lang='pt-br')



    ################################################## CORPO DO ASSENTO ###################################
    pdf.multi_cell(190, 10, f'              Aos {dia} dias do mês de {mes[datames]} do ano de {ano}, na Paróquia de {baptismo.paroquia}, municiopio de {baptismo.municipio},'
                        f' Diocese de  {baptismo.diocese} baptizei solenimente um indivíduo do sexo {baptismo.sexo} a quem dei o nome de {baptismo.nome} {baptismo.sobrenome}'
                        f' e que nasceu na na província de {baptismo.naturalidade}, municipio de {baptismo.municipio}, às ...... horas e ......... minutos'
                        f' do dia {dianascimento} do mês de {mes[mes_nascimento]} do ano de {anonascimento}.'
                        f'\n'
                        f'Filho de {baptismo.nomepai}, natural de {baptismo.naturalidadepai}, profissão {baptismo.profissaopai}, residente em {baptismo.residenciapai}, {baptismo.estadocivilpai}'
                        f' e de {baptismo.nomemae} natural de {baptismo.naturalidademae}, profissão {baptismo.profissaomae}, residente em {baptismo.residenciamae}, {baptismo.estadocivilmae}'
                        f'\n'
                        f'Neto paterno de  {baptismo.netopaternohomem} e de {baptismo.netopaternomulher} e neto materno de {baptismo.netomaternohomem} e de {baptismo.netomaternomulher}'
                        f'\n'
                        f'Foram Padrinhos {baptismo.padrinho}, baptizado na igreja {baptismo.padrinholocalbaptismo}, {baptismo.padrinhoestadocivil}, profissão {baptismo.padrinhoprofissao}, residente em {baptismo.padrinhoresidencia}'
                        f' e {baptismo.madrinha} baptizada na igreja {baptismo.madrinhalocalbaptismo}, {baptismo.madrinhaestadocivil} residente em {baptismo.madrinharesidencia} os quais sei serem os próprios'
                        f'\n'
                        f'           E, para constar lavrei em duplicado este assento, que, depois de ser lido e conferido perante:'
                        f'\n'
                        f'{baptismo.nomepai}'
                        f'\n'
                        f'{baptismo.nomemae}'
                        f'\n'
                        f'{baptismo.padrinho}'
                        f'\n'
                        f'{baptismo.madrinha}')

    pdf.set_xy(2, 10)
    pdf.multi_cell(58, 10, f'Assento Nº {baptismo.numero}'
                    f'\n'
                    f'Fl: {baptismo.folha}'
                    f'\n'  
                    f'{baptismo.nome.split()[0]} {baptismo.sobrenome}'
                    f'\n'
                    f'{datadia} - {datames} - {dataano}', 1, 1)

    pdf_conteudo = pdf.output(dest='S').encode('latin1')
    pdf_bytes = BytesIO(pdf_conteudo)

    return FileResponse( pdf_bytes, filename=f'Ref/{baptismo.diocese}/{baptismo.paroquia}/{pk}.pdf')
def casamento_pdf(request, pk):
    casamento = get_object_or_404(registoCasamento, pk=pk)
    pdf_casamento = FPDF('P', 'mm', 'A4')
    pdf_casamento.add_page()
    pdf_casamento.set_font('Arial', '', 12)
    pdf_casamento.set_fill_color(0, 0, 0)  # cor das celulas
    ###################################################     CABEÇALHO ####################################
    pdf_casamento.image("chancelaria/templates/verdade.jpeg", 1, 40, 210, 295)
    pdf_casamento.image("./chancelaria/verdadebeleza.jpeg", 84, 0, 50, 55)
    validacaoQRCODE = qrcode.make(f'qrcode_de_validação_de Assento de casamento do {casamento.nomenoivo} da '
                                  f'{casamento.nomenoiva}, número de registo {casamento.numero}, e esta na folha {casamento.folha}')
    validacaoQRCODE.save(f'Assento_casamento.png')
    pdf_casamento.image('Assento_casamento.png', 84, 245, 35, 35)

    pdf_casamento.cell(10, 30, '                                                           ', 0, 1, 'C', 0, 'False')
    pdf_casamento.cell(180, 7, '                 ARQUIDIOCESE DE LUANDA', 0, 1, 'C', 0, 'False')
    pdf_casamento.cell(180, 5, '                CHANCELARIA ARQUIDIOCESANA', 0, 1, 'C', 0, 'False')
    pdf_casamento.cell(180, 10, '                  ASSENTO DE BAPTISMO DIGITAL', 0, 1, 'C', 0, 'False')
    pdf_casamento.cell(180, 10, '                  ', 0, 1, 'C', 0, 'False')
    pdf_casamento.cell(180, 8, '                 ====== CÚRIA ARQUIDIOCESANA ======', 0, 1, 'C', 0, 'False')
    ################################################## CORPO DO ASSENTO ###################################
    pdf_casamento.multi_cell(190, 10, '0')
    pdf_casamento.set_xy(2, 10)
    pdf_casamento.multi_cell(58, 10, f'Assento Nº {casamento.numero}'
                           f'\n'
                           f'Fl {casamento.folha}'
                           f'\n'
                           f'{casamento.nomenoivo.split()[0]} {casamento.nomenoiva}'
                           f'\n'
                           f'{casamento.data}', 1, 1)


    pdf_conteudo = pdf_casamento.output(dest='S').encode('latin1')
    pdf_bytes = BytesIO(pdf_conteudo)

    return FileResponse(pdf_bytes, filename=f'Registo de baptismo número {pk}.pdf')


@login_required()
def paroquiaPesquisa(request):
    banco = paroquia.objects.all()
    paroquiabusca = paroquiaBusca(request.GET, queryset=banco)

    context = {

        'busca': paroquiabusca,
    }
    return (render(request, 'paroquiabusca.html', context))
from chancelaria.models import AssentoDeObito
def obito_pdf(request, pk):
    pdf = get_object_or_404(AssentoDeObito, pk=pk)
    pdf_obito = FPDF()
    pdf_obito.add_page('P', 'mm', 'A4')
    pdf_obito.set_font('Arial ', 'B', '14')
@login_required()
def centroPesquisa(request):
    banco = centro.objects.all()
    centrobusca = centroBusca(request.GET, queryset=banco)
    context = {
        'banco': banco,
        'busca': centrobusca,
        }
    return render(request, 'listagemcentro.html', context)

@login_required()
def updateparoquia(request, pk):
    banco = paroquia.objects.get(pk=pk)
    formulario = ParoquiaForm(request.POST or None, instance=banco)
    if formulario.is_valid():
        formulario.save()
        return redirect(home)
    contexto = {
        'formulario': formulario
    }
    return render(request, 'paroquia.html', contexto)

@login_required()
def provinciaCadastro(request):
    formulario = ProvinciaForm(request.POST or None, request.FILES )
    if formulario.is_valid():
        formulario.save()
        return redirect(home)
    context = {

            'formulario': formulario
        }
    return render(request, 'provinciaeclesiastica.html', context)

@login_required()
def dioceseCadastro(request):
        formulario = DioceseForm(request.POST, request.FILES )
        if formulario.is_valid():
            formulario.save()
            return redirect(home)
        context = {

            'formulario': formulario
        }
        return render(request, 'diocese.html', context)
@login_required()
def zonaCadastro(request):
        formulario = ZonaForm(request.POST, request.FILES )
        if formulario.is_valid():
            formulario.save()
            return redirect(home)
        context = {

            'formulario': formulario
        }
        return render(request, 'zona.html', context)
@login_required()
def listagemDiocese(request):
    banco = diocese.objects.all()
    context = {
        'banco': banco
    }
    return render(request, 'listagem.html', context)