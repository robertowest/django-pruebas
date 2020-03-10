from django.conf import settings

settings.INSTALLED_APPS += [
    'social_django',
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'


SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '...'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '...'

LOGIN_URL = '/accounts/login/google/'
