#!/usr/bin/env bash

#initialize_superset () {
#    USER_COUNT=$(fabmanager list-users --app superset | awk '/email/ {print}' | wc -l)
#    if [ "$?" ==  0 ] && [ $USER_COUNT == 0 ]; then
#        # Create an admin user (you will be prompted to set username, first and last name before setting a password)
#        fabmanager create-admin --app superset --username admin --firstname apache --lastname superset --email apache-superset@fab.com --password admin
#
#        # Initialize the database
#        superset db upgrade
#
#        # Load some data to play with
#        superset load_examples
#
#        # Create default roles and permissions
#        superset init
#
#        echo Initialized Apache-Superset. Happy Superset Exploration!
#    else
#        echo Apache-Superset Already Initialized.
#    fi
#}

superset db upgrade
echo Container deployment type "$NODE_TYPE"
if [ $NODE_TYPE = "server" ]; then
  gunicorn -w 5 -k gevent --timeout 180 -b 0.0.0.0:$SUPERSET_WEBSERVER_PORT --limit-request-line 0 --limit-request-field_size 0 "superset.app:create_app()"
elif [ $NODE_TYPE = "worker" ]; then
  celery worker --app=superset.tasks.celery_app:app --pool=prefork -O fair -c 4 &
  celery beat --app=superset.tasks.celery_app:app &
else
  echo Invalid node type "$NODE_TYPE"
  exit 1
fi





#gunicorn -w 5 -k gevent --timeout 180 -b 0.0.0.0:$SUPERSET_WEBSERVER_PORT --limit-request-line 0 --limit-request-field_size 0 "superset.app:create_app()" &