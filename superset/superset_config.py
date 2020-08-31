SQLALCHEMY_DATABASE_URI = "mysql://sage:crm$@ge@localhost/superset"
CACHE_WARMUP_USER = "whopper"
CACHE_DEFAULT_TIMEOUT = 60 * 60 * 24
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 60 * 60 * 24, # 1 day default (in secs)
    'CACHE_KEY_PREFIX': 'superset_results',
    'CACHE_REDIS_URL': 'redis://localhost:6379/0',
}

# python 3.6 required
#To start a Celery worker to leverage the configuration run:
# celery worker --app=superset.tasks.celery_app:app --pool=prefork -O fair -c 4

# To start a job which schedules periodic background jobs, run
# celery beat --app=superset.tasks.celery_app:app

# export SUPERSET_CONFIG_PATH="/home/turtle/saurabh_ws/env_superset1/lib/python3.6/site-packages/superset/superset_config.py"
