from django.contrib import admin
from chancelaria.models import registoBaptismo, registoCasamento, \
    livroBaptismo, paroquia, provincia, provinciaeclesiastica, diocese, arquidiocese, vigararia, centro, \
    congregacao, zona, livroCasamentoDuplicado, pessoa, AssentoDeObito

# Register your models here.

admin.site.register(livroBaptismo)
admin.site.register(registoBaptismo)
admin.site.register(provinciaeclesiastica)
admin.site.register(provincia)
admin.site.register(paroquia)
admin.site.register(AssentoDeObito)
admin.site.register(livroCasamentoDuplicado)
admin.site.register(registoCasamento)
admin.site.register(centro)
admin.site.register(pessoa)
admin.site.register(diocese)
admin.site.register(arquidiocese)
admin.site.register(vigararia)
admin.site.register(zona)
admin.site.register(congregacao)


