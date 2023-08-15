from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from chancelaria.models import paroquia
from chancelaria.models import registoBaptismo, livroCasamentoDuplicado, livroBaptismo
from chancelaria.models import centro, zona, diocese, arquidiocese, vigararia, provinciaeclesiastica, congregacao, registoBaptismo, registoCasamento

class LivroFormCasamento(ModelForm):
    class Meta:
        model = livroCasamentoDuplicado
        fields = ('__all__')
class LivroFormBaptismo(ModelForm):
    class Meta:
        model = livroBaptismo
        fields = ('__all__')

class BaptimoForm(ModelForm):

    class Meta:
        model = registoBaptismo
        fields = ('__all__')
class ParoquiaForm(ModelForm):
    class Meta:
        model = paroquia
        fields = ('__all__')
class centroForm(ModelForm):

    class Meta:
        model = centro
        fields = ('__all__')
class DioceseForm(ModelForm):

    class Meta:
        model = diocese
        fields = ('__all__')
class VigarariaForm(ModelForm):

    class Meta:
        model = vigararia
        fields = ('__all__')
class ZonaForm(ModelForm):

    class Meta:
        model = zona
        fields = ('__all__')
class CongregacaoForm(ModelForm):

    class Meta:
        model = congregacao
        fields = ('__all__')
class ArquidioceseForm(ModelForm):

    class Meta:
        model = arquidiocese
        fields = ('__all__')
class ProvinciaForm(ModelForm):

    class Meta:
        model = provinciaeclesiastica
        fields = ('__all__')


class registobaptismo(ModelForm):

    class Meta:

        model = registoBaptismo
        fields =('__all__')


class camentoForm(ModelForm):

    class Meta:
        model = registoCasamento
        fields =('__all__')

