#!/bin/bash
service nginx start
uwsgi --ini /app/deploy/portal_de_noticias.ini