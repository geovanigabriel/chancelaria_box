from django.contrib import admin
from chancelaria.models import registoBaptismo, registoCasamento,\
    livroBaptismo, livroCasamento, paroquia, provincia, provinciaeclesiastica, diocese, arquidiocese, vigararia, centro, congregacao, zona
# Register your models here.

admin.site.register(livroBaptismo)
admin.site.register(registoBaptismo)
admin.site.register(provinciaeclesiastica)
admin.site.register(provincia)
admin.site.register(paroquia)
admin.site.register(livroCasamento)
admin.site.register(registoCasamento)
admin.site.register(diocese)
admin.site.register(arquidiocese)
admin.site.register(vigararia)

