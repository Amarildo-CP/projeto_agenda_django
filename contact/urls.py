from contact import views
# Preciso antes de usar importar a 'views'
from django.urls import path


# Se eu tiver um outro 'app' com um nome 'index' tbm é só criar aqui um namespace pra esse:
app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
]
# Lembrar sempre de escolher um nome pra minha url
# Agora temos que referenciar esse 'urls' nos lugares necessários
# Temos que referenciar lá na 'urls' padrão do projeto (que está na pasta 'project')