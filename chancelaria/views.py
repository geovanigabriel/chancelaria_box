import datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from chancelaria.form import BaptimoForm, ParoquiaForm,  centroForm, VigarariaForm,  ArquidioceseForm, ProvinciaForm, CongregacaoForm, ZonaForm, DioceseForm, LivroFormBaptismo,  camentoForm, LivroFormCasamento
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponse, FileResponse
from chancelaria.models import paroquia, provincia, provinciaeclesiastica, registoBaptismo, registoCasamento, \
    livroBaptismo, diocese, congregacao, zona, vigararia, arquidiocese, centro, \
    livroCasamentoDuplicado
from fpdf import FPDF
from chancelaria.filters import dioceseBusca, paroquiaBusca, baptismoBusca, casamentoBusca
from io import BytesIO
from datetime import date



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
    return (render(request, 'duplicados.html', context))

@login_required()
def livro_baptismo(request, pk):
    banco = livroBaptismo.objects.get(pk=pk)
    context = {'livros': banco}
    return render(request, 'duplicados.html', context)







#################################      PERFIL      #####################################################
def perfil (request):
    pass



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
        'formulario': formulario
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
    formulario = camentoForm(request.POST or None, request.FILES)
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

    formulario = ArquidioceseForm(request.POST or None, request.FILES )
    if formulario.is_valid():
        formulario.save()
        return redirect(home)
    context = {

    'formulario': formulario
        }
    return render(request, 'arquidiocese.html', context)

@login_required()
def congregacaoCadastro(request):

    formulario = CongregacaoForm(request.POST or None, request.FILES )
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
    vigararia = VigarariaForm(request.POST or None)
    if vigararia.is_valid():
        vigararia.save()
        return redirect(home)
    contexto = {
        'formulario':vigararia
    }
    return render(request, 'cadastrar.html', contexto)

@login_required()
def CadastroDiocese(request):
    diocese = DioceseForm(request.POST or None)
    if diocese.is_valid():
        diocese.save()
        return redirect(home)
    contexto = {
        'formulario': diocese
    }
    return render(request, 'cadastrar.html', contexto)

@login_required()
def CadastroZona(request):
    zona = ZonaForm(request.POST or None)

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
def listagemCentro(request):
    banco = centro.objects.all()
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
    paroquia = ParoquiaForm(request.POST or None)
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

    paginator = Paginator(banco, 2)  # mostra 3 produtos por pagina
    page_number = request.GET.get('page')
    paginacao = paginator.get_page(page_number)
    context = {'banco': banco,
               'paginação': paginacao,
               'busca': busca,
               'provincia': bancoprovincia
               }
    return render(request, 'baptismobusca.html', context)



############################     P D F  BAPTISMO      #########################################
def baptismo_pdf(request, pk):
    baptismo = get_object_or_404(registoBaptismo, pk=pk)
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.set_fill_color(0, 0, 0) #cor das celulas
    ###################################################     CABEÇALHO ####################################
    pdf.image("chancelaria/templates/verdade.jpeg", 1, 40, 210, 295)
    pdf.image("./chancelaria/verdadebeleza.jpeg", 84, 0, 50, 50)


    pdf.cell(10, 25, '                                                           ', 0 , 1 , 'C',  0, 'False')
    pdf.cell(180, 10, '                 ARQUIDIOCESE DE LUANDA', 0 , 1 , 'C',  0, 'False')
    pdf.cell(180, 5, '                CHANCELARIA ARQUIDIOCESANA', 0 , 1 , 'C',  0, 'False')
    pdf.cell(180, 10, '                  ASSENTO DE BAPTISMO DIGITAL', 0 , 1 , 'C',  0, 'False')
    pdf.cell(180, 10, '                  ', 0 , 1 , 'C',  0, 'False')
    pdf.cell(180, 10, '               ====== CÚRIA ARQUIDIOCESANA ======', 0 , 1 , 'C',  0, 'False')
    ################################################## CORPO DO ASSENTO ###################################
    pdf.multi_cell(190, 10, f'{baptismo.data}, nesta igreja {baptismo.paroquia}, Municipio de {baptismo.municipio},'
                           f' {baptismo.diocese} baptizei solenimente um(a) individuo do sexo {baptismo.sexo}, a quem dei o nome de {baptismo.nome} {baptismo.sobrenome}'
                           f'e que nasceu em {baptismo.naturalidade}, no municipio da(o) {baptismo.municipio} no dia {baptismo.nascimento}.'
                           f'\n'
                        
                           f'Filho de {baptismo.nomepai}, natural de {baptismo.naturalidadepai},  {baptismo.profissaopai}, residente em {baptismo.residenciapai}, {baptismo.estadocivilpai}, '
                           f' e de {baptismo.nomemae} natural de {baptismo.naturalidademae}, {baptismo.profissaomae} residente em {baptismo.residenciamae}, {baptismo.estadocivilmae}.'
                           f'\n'
                           f'Neto paterno de {baptismo.netopaternohomem} e de {baptismo.netopaternomulher}, e neto materno {baptismo.netomaternohomem} e de {baptismo.netomaternomulher}.'
                           f'\n'
                
                           f'Foram Padrinhos {baptismo.padrinho}, baptizado na igreja {baptismo.padrinholocalbaptismo},   {baptismo.padrinhoestadocivil}, {baptismo.padrinhoprofissao}'
                           f' e {baptismo.madrinha} baptizado na igreja {baptismo.madrinhalocalbaptismo}, {baptismo.madrinhaestadocivil},  {baptismo.madrinhaprofissao}')
    pdf.set_xy(2, 10)
    pdf.multi_cell(58, 10, f'Nº {baptismo.numero}'
                     f'\n'
                    f'Fl {baptismo.folha}'
                    f'\n'  
                     f'{baptismo.nome.split()[0]} {baptismo.sobrenome}'
                     f'\n'
                     f'{baptismo.data}', 1, 1)
    #pdfimagem = FPDF('L', 'mm', 'A4')
    #pdfimagem.add_page()
    pdf_conteudo = pdf.output(dest='S').encode('latin1')
    pdf_bytes = BytesIO(pdf_conteudo)

    return FileResponse(pdf_bytes, filename=f'Registo de baptismo número {pk}.pdf')
def casamento_pdf(request, pk):
    casamento = get_object_or_404(registoCasamento, pk=pk)
    pdf_casamento = FPDF('P', 'mm', 'A4')
    pdf_casamento.add_page()
    pdf_casamento.set_font('Arial', 'B', 12)
    pdf_casamento.set_fill_color(240, 240, 240) #cor das celulas
    ###################################################     CABEÇALHO ####################################

    pdf_casamento.image("./chancelaria/serrra.jpg", 1, 1, 210, 297)

    pdf_casamento.cell(10, 40, '                                                                             ', 0 , 1 , 'C',  0, 'False')
    pdf_casamento.cell(180, 10, '                                                                                 ARQUIDIOCESE DE LUANDA', 0 , 1 , 'C',  0, 'False')
    pdf_casamento.cell(180, 5, '                                                                                 CHANCELARIA ARQUIDIOCESANA', 0 , 1 , 'C',  0, 'False')
    pdf_casamento.cell(180, 10, '                                                                                   ASSENTO DE BAPTISMO DIGITAL', 0 , 1 , 'C',  0, 'False')
    pdf_casamento.cell(180, 10, '                                                                                  ====== CÚRIA ARQUIDIOCESANA ======', 0 , 1 , 'C',  0, 'False')
    pdf_casamento.cell(10, 6, '                                                                             ', 0, 1, 'L', 0,'False')
    ################################################## CORPO DO ASSENTO ###################################
    pdf_casamento.multi_cell(210, 297, f'Aos {casamento.data} dias do mês de {casamento.data} de {casamento.data}, '
                            f'as {casamento.data} na igreja da paróquia {casamento.data}, em que é o paroco' )

    pdf_casamento.set_xy(236, 10)
    pdf_casamento.multi_cell(58, 10, f'Nº {casamento.numero}'
                    f'\n'
                    f'Fl nº{casamento.folha}'
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
        'banco': banco,
        'busca': paroquiabusca,
    }
    return render(request, 'paroquiabusca.html', context)

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