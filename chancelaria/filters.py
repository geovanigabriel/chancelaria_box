import django_filters
from chancelaria.models import paroquia,diocese, registoBaptismo, registoCasamento, livroBaptismo, livroCasamento



class dioceseBusca(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
         model = diocese
         fields = ['nome']

class paroquiaBusca(django_filters.FilterSet):

    nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = paroquia
        fields = ['nome']


class baptismoBusca(django_filters.FilterSet):

    nome = django_filters.CharFilter(lookup_expr='icontains')
    sobrenome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = registoBaptismo
        fields = ['nome', 'sobrenome']


class casamentoBusca(django_filters.FilterSet):

    nomenoivo = django_filters.CharFilter(lookup_expr='icontains')
    nomenoiva = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = registoCasamento
        fields = ['nomenoivo', 'nomenoiva']
