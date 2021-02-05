FROM python:3.6
MAINTAINER Keshav Saini <keshav.s@turtlemint.com>
ARG GIT_BRANCH=develop
ENV FLASK_APP=superset
ENV NODE_TYPE=server
ENV OAUTH_ENABLED=0
ENV SUPERSET_CONFIG_PATH="/usr/local/lib/python3.6/site-packages/superset/superset_config.py"
ENV SQLALCHEMY_DATABASE_URI='mysql://sage:crm$@ge@172.32.1.97/superset1'
ENV REDIS_SERVER_IP=172.32.1.64
ENV SUPERSET_WEBSERVER_PROTOCOL="http"
ENV SUPERSET_WEBSERVER_ADDRESS="0.0.0.0"
ENV SUPERSET_WEBSERVER_PORT=8088
COPY requirements.txt ./
COPY docker-entrypoint.sh ./
RUN pip install -r requirements.txt \
    && pip install --upgrade --no-deps --force-reinstall git+https://github.com/Turtlemint-India/superset.git@${GIT_BRANCH}
CMD ["sh", "docker-entrypoint.sh"]