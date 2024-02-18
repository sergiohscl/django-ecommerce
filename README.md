# Projeto E-commerce 
Um projeto extremamente simples de e-commerce (ainda incompleto) feito com 
Django 5.0.1 e Python 3.12.1.

### Conteúdo educacional
Este conteúdo foi criado no [Curso de Python 3 - Do Básico Ao Avançado (Completo)](https://www.udemy.com/course/python-3-do-zero-ao-avancado/) sem a intenção de 
ser utilizado em produção, mas como recurso educacional ensinado no meu curso.

Isso não impede que você baixe, altere, use e/ou distribua o seu conteúdo conforme preferir.

### Este projeto NÃO inclui
Abaixo uma lista de recursos que não adicionei ainda e que você pode me ajudar a adicionar.

- Combinações de variações de produto (tem apenas uma variação)
- Cupons de desconto no carrinho de compras
- Cálculo de frete
- Métodos de pagamento (MercadoPago, PayPal, PagSeguro, enfim...)

### TODOs
Abaixo uma lista do que adicionei ou ainda pretendo adicionar.

- [x] Model produtos
- [x] Model variações
- [x] Listagem e detalhes de produtos e variações
- [x] Carrinho de compras baseado em session
- [x] Remover produtos do carrinho
- [x] Model perfil (criar e atualizar)
- [x] Login e Logout do cliente
- [x] Registrar pedido do cliente
- [x] Página de pagamento

### Tutorial para iniciantes
Abaixo uma lista de comandos para clonar e configurar este projeto na sua 
máquina local:

- Instalar git (Windows, Linux e Mac) e depois:

```
git clone https://github.com/sergiohscl/django-ecommerce.git
```

- Para **Windows**:

```
cd django-simple-ecommerce
python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel --user
python -m pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

- Para **Linux**:

```
cd django-simple-ecommerce
python3.7 -m venv venv
. venv/bin/activate
pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

- Para **Mac**

```
cd django-simple-ecommerce
python -m venv venv
. venv/bin/activate
pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

Pronto!

## ambiente virtual
    python3 -m venv venv

## ativar ambiente virtual
    . venv/bin/activate

## install django
    pip install django

## install django-crispy-forms
    pip install django-crispy-forms

## install pillow
    pip install pillow

## install django-debug-toolbar
    pip install django-debug-toolbar

## Iniciando project django
    django-admin startproject <nome-project> .

## Criar o arquivo requirements.txt
    pip freeze > requirements.txt

## Instale as dependências no projeto
    pip install -r requirements.txt

## install app
    python manage.py startapp <nome-app>

## Migrando a base de dados do Django
    python manage.py makemigrations
    python manage.py migrate

## Criando e modificando a senha de um super usuário
    python manage.py createsuperuser
    python manage.py changepassword USERNAME

## Rodando django-admin
    python manage.py runserver

# configure settings
## imports
    import os
    from django.contrib.messages import constants

## templates   
    TEMPLATES = 'DIRS': [os.path.join(BASE_DIR, 'templates')]

## language e timezone
    LANGUAGE_CODE = "pt-BR"
    TIME_ZONE = "America/Sao_Paulo"

## static files:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)

    STATIC_ROOT = os.path.join('static')

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

## Django message
    MESSAGE_TAGS = {
        constants.DEBUG: 'alert-primary',
        constants.ERROR: 'alert-danger',
        constants.SUCCESS: 'alert-success',
        constants.INFO: 'alert-info',
        constants.WARNING: 'alert-warning',
    }

# configurar urls
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

