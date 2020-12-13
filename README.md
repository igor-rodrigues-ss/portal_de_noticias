# Portal de Notícias

## API de notícias utilizando Python3.9/Flask e MongoDB

## Pre-requisitos:
- Docker
- Docker-Compose
- Python 3.9
- MongoDB
- Poetry


### Ambiente de desenvolvimento
- Preparando o ambiente.
```sh
cd portal_de_noticias
mkvirtualenv portal_de_noticias -p python3.9
poetry install --dev
```
- Crie um novo container do docker com mongodb.
- Configure as crendenciais de acesso no arquivo: config.env.
```sh
vim portal_de_noticias/config.env
```
- Executando a aplicação em desenvolvimento:
```sh
python dev.py
# acesse: http://localhost:5000
```
- Executando testes:
```sh
pytest -v
```

### Deploy
- Atualize o arquivo config.env com as variáveis do ambiente em questão.
```sh
vim portal_de_noticias/config.env
```
- Acesse o diretório **deploy** e execute o script *deploy.sh*.
```sh
cd portal_de_noticias/deploy
./deploy.sh
# acesse: http://localhost:5000
```
- Após a execução do *deploy.sh* será instanciado um container da aplicação (api) e da base de dados (mongo) configurados por meio do arquivo **portal_de_noticias/config.env**.

- Para visualizar o logs da aplicação execute :
```sh
docker logs -f api
```
