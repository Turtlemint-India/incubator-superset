import os

from flask_appbuilder.const import AUTH_OAUTH

from superset.custom_sso_security_manager import CustomSsoSecurityManager

SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
CACHE_WARMUP_USER = "whopper"
CACHE_DEFAULT_TIMEOUT = 60 * 60 * 6
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 60 * 60 * 6,  # 6 hr default (in secs)
    'CACHE_KEY_PREFIX': 'superset_results',
    'CACHE_REDIS_URL': 'redis://localhost:6379/0',
}

CUSTOM_SECURITY_MANAGER = CustomSsoSecurityManager
AUTH_TYPE = AUTH_OAUTH
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Gamma"

OAUTH_PROVIDERS = [
    {'name': 'google', 'icon': 'fa-google', 'token_key': 'access_token', 'whitelist': ['@turtlemint.com'],
     'remote_app': {
         'client_id': '78989321337-5e44ugm9ev8davgp7591njjv7o81naoc.apps.googleusercontent.com',
         'client_secret': '-ul9faMKxh5ddwmXrchaUewr',
         'api_base_url': 'https://www.googleapis.com/oauth2/v2/',
         'client_kwargs': {
             'scope': 'email profile'
         },
         'request_token_url': None,
         'access_token_url': 'https://accounts.google.com/o/oauth2/token',
         'authorize_url': 'https://accounts.google.com/o/oauth2/auth'}
     }
]
