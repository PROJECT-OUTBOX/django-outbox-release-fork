_Z='MAIN_DOMAIN'
_Y='secret'
_X='client_id'
_W='youtube'
_V='plain-text'
_U='extraPlugins'
_T='pasteFilter'
_S='toolbarCanCollapse'
_R='toolbar'
_Q='bootstrap4'
_P='CSRF_TRUSTED_ORIGINS'
_O='MEDIA_ROOT'
_N='STATIC_ROOT'
_M='DB_NAME'
_L='ENGINE'
_K='templates'
_J='allauth'
_I='ALLOWED_HOSTS'
_H='SECRET_KEY'
_G='DB_PASSWORD'
_F='/dashboard/'
_E='default'
_D='id'
_C=False
_B='NAME'
_A=True
from pathlib import Path
import os
BASE_DIR=Path(__file__).resolve().parent.parent
from encryption import OutboxEncryption
lib=OutboxEncryption(BASE_DIR)
mplaint_key=[_G,_H]
mplaint_list=[_I]
key=lib.dec_environ(mplaint_key,mplaint_list)
if not key:raise Exception('No data found in environment!')
SECRET_KEY=key[_H]
DEBUG=key['DEBUG']
UNDER_CONSTRUCTION=key['UNDER_CONSTRUCTION']
ALLOWED_HOSTS=key[_I]
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','django.contrib.sites','django.contrib.humanize','core','education','region','menu','ckeditor','ckeditor_uploader','parler','hitcount','crispy_forms','corsheaders',_J,'allauth.account','allauth.socialaccount','allauth.socialaccount.providers.google','allauth.socialaccount.providers.facebook','allauth.socialaccount.providers.github','captcha','multiselectfield','debug_toolbar']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.locale.LocaleMiddleware','corsheaders.middleware.CorsMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware','debug_toolbar.middleware.DebugToolbarMiddleware','education.request_exposer.RequestExposerMiddleware']
ROOT_URLCONF='django_outbox.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[os.path.join(BASE_DIR,_K),os.path.join(BASE_DIR,_K,_J)],'APP_DIRS':_A,'OPTIONS':{'context_processors':['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages','education.processor.context_outbox','backend.processor.context_outbox','backend.processor.get_main_domain','backend.processor.site_id']}}]
WSGI_APPLICATION='django_outbox.wsgi.application'
db_engine=key['DB_ENGINE']
if'sqlite3'in db_engine:DATABASES={_E:{_L:db_engine,_B:key[_M]}}
else:DATABASES={_E:{_L:db_engine,_B:key[_M],'USER':key['DB_USER'],'PASSWORD':key[_G],'HOST':key['DB_HOST'],'PORT':key['DB_PORT']}}
AUTH_PASSWORD_VALIDATORS=[{_B:'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},{_B:'django.contrib.auth.password_validation.MinimumLengthValidator'},{_B:'django.contrib.auth.password_validation.CommonPasswordValidator'},{_B:'django.contrib.auth.password_validation.NumericPasswordValidator'}]
LANGUAGE_CODE=_D
TIME_ZONE='Asia/Makassar'
USE_I18N=_A
USE_L10N=_A
USE_TZ=_C
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
STATIC_URL='/static/'
STATIC_ROOT=key[_N]if key.get(_N)else os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
MEDIA_URL='/media/'
MEDIA_ROOT=key[_O]if key.get(_O)else os.path.join(BASE_DIR,'media')
tmp=key.get(_P)
if tmp:CSRF_TRUSTED_ORIGINS=key[_P]
SITE_ID=1
LOGIN_REDIRECT_URL=_F
LOGOUT_REDIRECT_URL=_F
IMPORT_EXPORT_USE_TRANSACTIONS=_A
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
AUTH_USER_MODEL='core.User'
EMAIL_USE_TLS=_A
EMAIL_USE_SSL=_C
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='auto.email.activation@gmail.com'
EMAIL_HOST_PASSWORD='rinapuspitadewi'
EMAIL_PORT=587
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS=_C
ACCOUNT_LOGIN_ON_PASSWORD_RESET=_A
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE=_A
ACCOUNT_USERNAME_MIN_LENGTH=4
ACCOUNT_SESSION_REMEMBER=_A
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=1
ACCOUNT_EMAIL_REQUIRED=_A
ACCOUNT_LOGIN_ATTEMPTS_LIMIT=5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT=86400
ACCOUNT_LOGOUT_REDIRECT_URL=_F
ACCOUNT_AUTHENTICATION_METHOD='email'
ACCOUNT_UNIQUE_EMAIL=_A
ACCOUNT_USER_MODEL_USERNAME_FIELD=None
ACCOUNT_USERNAME_REQUIRED=_C
ACCOUNT_LOGOUT_ON_GET=_A
SOCIALACCOUNT_LOGIN_ON_GET=_C
ACCOUNT_FORMS={'login':'core.forms.UserLoginForm','reset_password':'core.forms.UserResetPasswordForm','signup':'core.forms.UserSignupForm'}
CRISPY_TEMPLATE_PACK=_Q
CKEDITOR_UPLOAD_PATH='uploads/'
CKEDITOR_BASEPATH='/static/ckeditor/ckeditor/'
CKEDITOR_RESTRICT_BY_USER=_A
CKEDITOR_CONFIGS={_E:{'width':'100%',_R:'full',_S:_A,_T:_V,'removePlugins':('exportpdf','scayt'),_U:','.join(['texttransform','html5audio','html5video','wordcount',_W,'embedsemantic','autolink','codesnippet','previewgoogledrive','previewdocument'])},'embed_video':{_U:','.join([_W]),_S:_A,_T:_V,_R:'Custom','toolbar_Custom':[['Source','Iframe'],['Youtube']]}}
SOCIALACCOUNT_PROVIDERS={'github':{'APP':{_X:'6c0e925336cace458a21',_Y:'e5e0a76006524a3b49e9c0593ac29f2d1ee8c354','key':''}},'facebook':{'APP':{_X:'1582129178867576',_Y:'6edc1f622ef5ba62ec8d8e54d8228ef8','key':''}},'google':{'SCOPE':['profile','email'],'AUTH_PARAMS':{'access_type':'online'}}}
from django.utils.translation import gettext_lazy as _
LANGUAGES=(_D,_('Indonesia')),('en',_('English'))
LOCALE_PATHS=[os.path.join(BASE_DIR,'locale')]
PARLER_DEFAULT_LANGUAGE_CODE=_D
PARLER_LANGUAGES={1:({'code':_D},{'code':'en'}),_E:{'fallbacks':[_D],'hide_untranslated':_C}}
CRISPY_TEMPLATE_PACK=_Q
HITCOUNT_KEEP_HIT_IN_DATABASE={'months':3}
HITCOUNT_KEEP_HIT_ACTIVE={'minutes':1}
AUTHENTICATION_BACKENDS=['allauth.account.auth_backends.AuthenticationBackend']
tmp=key.get(_Z)
MAIN_DOMAIN=key[_Z]if tmp else'127.0.0.1:8000'
CACHES_TIMEOUT=24*60*60
SENDGRID_API_KEY='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'
RECAPTCHA_PUBLIC_KEY='6Le_ixcmAAAAABbCXol2K5HaE0vY906KKFrFm0PX'
RECAPTCHA_PRIVATE_KEY='6Le_ixcmAAAAAFeqpjBlKQcgDkPxZjMmk--cuEZU'
INTERNAL_IPS=['127.0.0.1']