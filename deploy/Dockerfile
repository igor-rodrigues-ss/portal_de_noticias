FROM python:3.9

RUN apt-get update
RUN apt install -y nginx

###### Configurando UTF-8 ##########
RUN apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8


###### Configurando Data e Hora ##########
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update && apt upgrade tzdata -y


###### Instalando Poetry
RUN apt-get install curl && \
    curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python


##### Configurando a aplicacao #########
RUN mkdir -p /var/log/uwsgi/
COPY . /app
RUN cp /app/deploy/portal_de_noticias.conf /etc/nginx/conf.d
RUN chmod +x /app/deploy/start.sh
WORKDIR /app
RUN /bin/bash -c "source /root/.poetry/env && \
	poetry config virtualenvs.create false --local && \
	poetry install --no-dev"


EXPOSE 5000

CMD ["./deploy/start.sh"]
