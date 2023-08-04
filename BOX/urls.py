from django.contrib import admin
from django.urls import path, include, re_path
from allauth.account import views
from chancelaria.views import home, delete, livro, arquidioceseCadastro, zonaCadastro, centroCadastro, dioceseCadastro, updateparoquia, \
    paroquiaCadastro, vigarariaCadastro, provinciaCadastro, baptismocaCadastro, congregacaoCadastro, CadastroZona, \
    CadastroVigararia, CadastroParoquia, CadastroDiocese, listagemParoquia, listagemVigararia, listagemZona, \
    listagemDiocese, listagemArquidiocese, listagemCongregacao, listagemCentro, listagemProvinciaEclesiastica, \
    livroCasamento, livroBaptismo,livrobaptismo ,lista,export_pdf_baptismo,casamentopdf,paroquiaBusca, updateCasamento,paroquiaPesquisa, updateBaptismo, baptismoPesquisa, registocasamento, casamentoPesquisa

urlpatterns = [
    path('admin/', admin.site.urls, name= 'admin'),
    path('accounts/', include('allauth.urls')),
    path('', home, name='url_home'),
    path('listagem/', lista, name='url_listagem'),
    path('livro_baptismo/', livro, name='url_listagem_livro'),

    path('updateparoquia/<int:pk>/', updateparoquia, name='url_update'),
    path('updatebaptismo/<int:pk>/', updateBaptismo, name='url_update_baptismo'),
    path('updatecasamento/<int:pk>/', updateCasamento, name='url_update_casamento'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    path('cadastro_livro_casamento/', livroCasamento, name='url_livro_casamento'),
    path('cadastro_livro_baptismo/', livrobaptismo, name='url_livro_baptismo'),
    path('cadastro_baptismo/', baptismocaCadastro, name='url_baptismo'),
    path('cadastro_casamento/', registocasamento, name='url_casamento'),



##############################   FILTRO DE INFORMAÇÃO ###############



    path('pesquisa_baptismo/', baptismoPesquisa, name='url_pesquisa_baptismo'),
    path('pdf_casamento/', casamentopdf, name='url_pdf_casamento'),
    path('pdf_baptismo/<int:pk>/', export_pdf_baptismo, name='url_pdf_baptismo'),
    path('pesquisa_baptismo/', baptismoPesquisa, name='url_pesquisa_baptismo'),
    path('listagem_paroquia/', paroquiaPesquisa, name='url_listagem_paroquia'),
    path('pesquisa_casamento/', casamentoPesquisa, name='url_pesquisa_casamento'),



############################# CADASTRO DE INSTITUIÇOES ###################


    path('cadastro_paroquia/', paroquiaCadastro, name='url_paroquia'),
    path('cadastro_centro/', centroCadastro, name='url_centro'),
    path('cadastro_vigararia/', vigarariaCadastro, name='url_vigararia'),
    path('cadastro_zona/', zonaCadastro, name='url_zona'),
    path('cadastro_diocese/', dioceseCadastro, name='url_diocese'),
    path('cadastro_arquidiocese/', arquidioceseCadastro, name='url_arquidiocese'),
    path('cadastro_padre/', provinciaCadastro, name='url_padre'),
    path('cadastro_congregacao/', congregacaoCadastro, name='url_congregacao'),
    path('cadastro_proncincia_ecleciastica/', provinciaCadastro, name='url_provincia'),



############################# ALLAUTH #####################################
    path("signup/", views.signup, name="account_signup"),
    path("login/", views.login, name="account_login"),
    path("logout/", views.logout, name="account_logout"),
    path("password/change/", views.password_change, name="account_change_password"),
    path("password/set/", views.password_set, name="account_set_password"),
    path("inactive/", views.account_inactive, name="account_inactive"),

    # E-mail
    path("email/", views.email, name="account_email"),
    path("confirm-email/", views.email_verification_sent, name="account_email_verification_sent"),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email, name="account_confirm_email"),

    # password reset
    path("password/reset/", views.password_reset, name="account_reset_password"),
    path( "password/reset/done/", views.password_reset_done, name="account_reset_password_done"),
    re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", views.password_reset_from_key, name="account_reset_password_from_key"),
    path("password/reset/key/done/", views.password_reset_from_key_done, name="account_reset_password_from_key_done"),

]
