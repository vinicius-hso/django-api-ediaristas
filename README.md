# Step-by-step commands

## CRUD

#### Create a venv
`python3 -m venv env`

#### Activate venv
`source env/bin/activate`

#### Install Django
`python3 -m pip install Django`

#### Check dependencies
`pip freeze`

```bash
asgiref==3.4.1
Django==3.2.8
pytz==2021.3
sqlparse==0.4.2
typing-extensions==3.10.0.2
```

#### Start Django admin project
`django-admin startproject <project_name>`

#### Start Web Project
`python manage.py startapp web`

#### Run server
`python manage.py runserver`

#### Install Pillow to work with images (ImageField)
`pip install Pillow`

#### Make Migrations
Registre o app web em settings e rode:
`python manage.py makemigrations`

#### Migrate
Criar as tabelas no banco
`python manage.py migrate`

#### Templates Directory
Criar o diretório template no app web
`mkdir templates`

#### Form Directory
Criar um diretório para form no app web
`mkdir form`

#### Urls Script
Criar um arquivo urls.py no app web
`touch urls.py`

#### Settings - Media
```bash
# settings.py
# depois de STATIC_URL = '/static'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media'
```

#### Install Crispy Forms
`pip install django-crispy-forms`

#### Settings
```bash
INSTALLED_APPS = [
    '...',
    'crispy_forms',
    'web'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
```

#### Add Bootstrap CDN
At base.html

`<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">`

#### Add JQuery CDN
At base.html
`<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>`

#### Add JQuery Mask CDN
At base.html
`<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.11.2/jquery.mask.min.js" integrity="sha512-Y/GIYsd+LaQm6bGysIClyez2HGCIN1yrs94wUrHoRAD5RSURkqqVQEU6mM51O90hqS80ABFTGtiDpSXd2O05nw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>`

#### Install Easy Mask Package
`pip install easy-mask==1.1.3`

#### Settings - register
```bash
INSTALLED_APPS = [
    '...',
    'easy_mask',
    'web'
]
```

#### Services Directory
Criar um diretório para services no app web
`mkdir services`

#### Install Requests
`python -m pip install requests`

## API

#### Create app API
`python manage.py startapp api`

#### Settings - register
```bash
INSTALLED_APPS = [
    '...',
    'web',
    'api'
]
```

#### Install Django Rest Framework
`pip install djangorestframework`

#### Install Django Cors Headers
`python -m pip install django-cors-headers`

#### Settings - register
```bash
INSTALLED_APPS = [
    '...',
    'corsheaders',
    '...',
]

CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    '...',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    '...',
]
```