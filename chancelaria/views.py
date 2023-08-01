from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from chancelaria.form import BaptimoForm, ParoquiaForm,  centroForm, VigarariaForm,  ArquidioceseForm, ProvinciaForm, CongregacaoForm, ZonaForm, DioceseForm, LivroFormBaptismo,  registocamento, LivroFormCasamento


from chancelaria.models import paroquia, provincia, provinciaeclesiastica, registoBaptismo, registoCasamento, \
    livroBaptismo, diocese,  congregacao, zona, vigararia, arquidiocese, centro


import io
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import  canvas
from django.http import FileResponse

from chancelaria.filters import dioceseBusca, paroquiaBusca, baptismoBusca, casamentoBusca

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



############################     P D F #########################################
@login_required()
def baptismopdf(request, pk):
    pdf = io.BytesIO()
    canva = canvas.Canvas(pdf, pagesize=letter, bottomup=0)
    pdfobjecto = canva.beginText()
    pdfobjecto.setTextOrigin(inch, inch)
    pdfobjecto.setFont('Helvetica', 16)

    banco = registoBaptismo.objects.get(pk=pk)

    registo = []



    for assunto in registo:
        pdfobjecto.textLine(assunto)


    canva.drawText(pdfobjecto)
    canva.showPage()
    canva.save()
    pdf.seek(0)

    return FileResponse( request, pdf, as_attachment=True, filename='Registo.pdf')

@login_required()
def casamentopdf( request):
    pdf = io.BytesIO()
    canva = canvas.Canvas(pdf, pagesize=letter, bottomup=0)
    pdfobjecto = canva.beginText()
    pdfobjecto.setTextOrigin(inch, inch)
    pdfobjecto.setFont('Helvetica', 16)

    banco = registoCasamento.objects.all()
    registo = []

    for linha in banco:
        registo.append(linha.nome)

    for assunto in registo:
        pdfobjecto.textLine(assunto)


    canva.drawText(pdfobjecto)
    canva.showPage()
    canva.save()
    pdf.seek(0)

    return FileResponse(pdf, as_attachment=True, filename='Registo.pdf')

@login_required()
def lista(request):
    diocesebanco = diocese.objects.all()
    busca = dioceseBusca(request.GET, queryset=diocesebanco)
    context = { 'diocese': diocesebanco, 'busca': busca}

    return render(request, 'listagem.html', context)

@login_required()
def livro(request):

    banco = livroBaptismo.objects.all()
    context = {'livros': banco}
    return render(request, 'livros.html', context)

@login_required()
def paroquiaPesquisa(request):
    banco = paroquia.objects.all()
    paroquiabusca = paroquiaBusca(request.GET, queryset=banco)
    paginate_by = 20
    context = {
        'banco': banco,
        'busca': paroquiabusca,
        'paginate': paginate_by
    }
    return render(request, 'paroquiabusca.html', context)





#################################  PERFIL      #########################################################################
def perfil (request):
    pass



#################################   UPDATES    #########################################################################
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
    return render(request, 'paroquia.html', contexto)\
        @login_required()
def updateCasamento(request, pk):
    banco = paroquia.objects.get(pk=pk)
    formulario = ParoquiaForm(request.POST or None, instance=banco)
    if formulario.is_valid():
        formulario.save()
        return redirect(home)
    contexto = {
        'formulario': formulario
    }
    return render(request, 'casamentobusca.html', contexto)

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
def home(request):

    return render(request, 'home.html')

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
    formulario = registocamento(request.POST or None, request.FILES)
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
def livroCasamento(request):
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
def CadastroParoquia(request):
    paroquia = ParoquiaForm(request.POST or None)
    if paroquia.is_valid():
        paroquia.save()
        return redirect(home)
    contexto = {
        'formulario': paroquia
    }
    return render(request, 'paroquia.html', contexto)

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
def listagemDiocese(request):
    banco = diocese.objects.all()
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

