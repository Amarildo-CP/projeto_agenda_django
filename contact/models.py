from django.db import models
from django.utils import timezone

# id (primary key - automático). Lembrando que é usado para buscar valores na base de dados
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

# O que tem campo específico utilizamos o campo específico
# O que não tem campo específico colocamos 'string'
# O que está entre () são os campos que serão utilizados
# string é limitado, até 255 caracteres no máximo
# Se eu precisar de uma coisa maior do que 255 caracteres eu utilizo um campo de 'text'
# Isso é algo forçado pelo próprio programa

# 'category' será outro 'model', ou seja, outra tabela na base de dados.
# É como se o contado dependesse dessa categoria existir

# 'owner' será o dono do contato, quem criou o contato na tabela

# Para criar um model eu crio uma classe:
# O nome dessa classe (da coisa que vou criar) tem que vir no singular
# Essa classe vai herdar do módulo que foi importado (models.Model)
# Essa será nossa tabela, que será utilizada para fazer o CRUD
# Vamos ter que migrar essa model para gerar a tebela na base de dados
# Quando crio uma tabela na base de dados um campo que é primordial é o 'ID'
# Esse id é gerado automaticamente pelo Django
class Contact(models.Model): # Criação da tabela
# Agora preciso criar um campo pra essa tabela. Utilizo 'model.field alguma coisa'
# 'first_name' será o nome do campo
# No campo do django 'string = CharField'. Tudo o que for string pode ser configurado dessa mesma forma com o mesmo tamanho
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50, blank= True)
    phone = models.CharField(max_length= 50)
    email = models.EmailField(max_length= 254, blank= True) # 'blank= True' se eu quiser colocar o campo como opcional
# Todos esses campos (de texto) que estão sendo criados dessa maneira são por padrão obrigatórios 
# Eu não conseguiria registrar uma pessoa sem algum desses campos
# 'created_date' é a data em que o contato foi criado. Esse campo não deve ser editado pelo utilizador
# Esse campo tem que ser preenchido automaticamente
    created_date = models.DateTimeField(default= timezone.now) # Essa função não é executada aqui
# É o django que vai executar essa função no momento em que o contato for registrado
    description = models.TextField(blank= True) # Aqui eu não preciso passar nada de limitação de tamanho caso eu não queira

# Qualquer coisa que eu mudar no meu model tenho que executar o comando: 'python manage.py makemigrations'
# O django tem que ver o que eu alterei no meu model e se precisar gerar uma migração pra depois aplicar essa migração
# O código para aplicar essa migração: 'python manage.py migrate'
# Aplicar significa salvar tudo isso na minha base de dados
