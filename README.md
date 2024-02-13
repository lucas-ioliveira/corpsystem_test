<h1 align="center" style="font-weight: bold;">CORPSYSTEM ERP (TESTE DE CÓDIGO) 💻</h1>


Nesse repositório contém um projeto realizado o back-end com Python, Django Rest Framework, Docker e front-end Vue.JS. O Projeto consiste em uma Api rest para um sistema ERP contendo os módulos de login, clientes, produto, grupo do produto, vendas e relatório. 


<h2>Pré-requisitos</h2>

- [Python](https://www.python.org/) 
- [Docker](https://www.docker.com/) 
- [NodeJS](https://nodejs.org/en)



<h2>Clone</h2>

Como clonar o projeto:

- HTTPS

```bash
git clone https://github.com/lucas-ioliveira/corpsystem_test.git
```


<h2 id="started">🚀 Primeiros passos</h2>

<p>Back-End</p>

- Isso fará com que todas as dependências sejam instaladas e um container docker seja executado.
- Basta entrar no diretório backend acessar o terminal e rodar o comando: 

```bash
docker compose -f docker-compose-dev.yaml up --build
```

<p>Fron-End</p>

- Basta entrar no diretório frontend acessar o terminal e rodar o comando: 

```bash
sudo npm install -g @vue/cli
```

```bash
npm run serve
```

<h2 id="routes">📍 API Endpoints</h2>

<p>Após rodar o projeto é possivel acessar a rota: (/swagger/) onde terá acesso ao swagger e uma documentação mais detalhada e também testar os endpoints.</p>

**LOGIN**
   
| <kbd>POST /login</kbd> | Autenticar usuário na API.


**REQUEST**
```json
{
  "username": "lucas.dev",
  "password": "1234567"
}
```

**RESPONSE**
```json
{
  "token": "OwoMRHsaQwyAgVoc3OXmL1JhMVUYXGGBbCTK0GBgiYitwQwjf0gVoBmkbuyy0pSi"
}
```
<br>

**CLIENTES**

| <kbd>GET /clientes/:</kbd> | Coletar todos os clientes ativos

**RESPONSE**
```json
{
    "id": 1,
    "nome": "string-teste-1",
    "sobrenome": "string",
    "email": "user@example.com",
    "dt_aniversario": "2024-02-12",
    "telefone": "string",
    "status": true,
    "cep": "string",
    "logradouro": "string",
    "bairro": "string",
    "cidade": "string",
    "complemento": "string",
    "uf": "st",
    "dt_criacao": "2024-02-12",
    "dt_atualizacao": "2024-02-12"
  },
```
<br>

| <kbd>GET /clientes/detalhes/1:</kbd> | Coletar o cliente ativo pelo ID.

**REQUEST**
```json
{
  "id": 1
}
```

**RESPONSE**
```json
{
    "id": 1,
    "nome": "string-teste-1",
    "sobrenome": "string",
    "email": "user@example.com",
    "dt_aniversario": "2024-02-12",
    "telefone": "string",
    "status": true,
    "cep": "string",
    "logradouro": "string",
    "bairro": "string",
    "cidade": "string",
    "complemento": "string",
    "uf": "st",
    "dt_criacao": "2024-02-12",
    "dt_atualizacao": "2024-02-12"
  },
```
<br>

| <kbd>POST /clientes/:</kbd> | Cria um cliente.

**REQUEST**
```json
{
  "nome": "string",
  "sobrenome": "string",
  "email": "user@example.com",
  "dt_aniversario": "2024-02-13",
  "telefone": "string",
  "status": true,
  "cep": "string",
  "logradouro": "string",
  "bairro": "string",
  "cidade": "string",
  "complemento": "string",
  "uf": "st"
}
```

**RESPONSE**
```json
{
  "id": 3,
  "nome": "string",
  "sobrenome": "string",
  "email": "user@example.com",
  "dt_aniversario": "2024-02-13",
  "telefone": "string",
  "status": true,
  "cep": "string",
  "logradouro": "string",
  "bairro": "string",
  "cidade": "string",
  "complemento": "string",
  "uf": "st",
  "dt_criacao": "2024-02-13",
  "dt_atualizacao": "2024-02-13"
}
  ```
<br>

| <kbd>PATCH /clientes/detalhes/1:</kbd> | Atualiza os dados do cliente (só atualiza o campo desejado).

**REQUEST**
```json
{
  "id": 1
}
```

**RESPONSE**
```json
{
    "id": 1,
    "nome": "string-teste-1",
    "sobrenome": "string",
    "email": "user@example.com",
    "dt_aniversario": "2024-02-12",
    "telefone": "string",
    "status": true,
    "cep": "string",
    "logradouro": "string",
    "bairro": "string",
    "cidade": "string",
    "complemento": "string",
    "uf": "st",
    "dt_criacao": "2024-02-12",
    "dt_atualizacao": "2024-02-12"
  },
```
<br>

| <kbd>DELETE /clientes/detalhes/1:</kbd> | Atualiza os dados do cliente (só atualiza o campo desejado).

**REQUEST**
```json
{
  "id": 1
}
```

**RESPONSE**
```json
status  204 no content
```

<br>

**RELATORIOS**

| <kbd>POST /relatorios/exportar/:</kbd> | Exporta um relatório em pdf ou excel a escolha do usuário com filtros (opcionais, porém necessita um parâmetro) data, vendedor ou cliente.

```json
{
  "data": "opcional", 
  "vendedor": "opcional",
  "cliente": "opcional",
  "opcao ": "pdf/excel",
}
```

**RESPONSE**
```json
Downloand do arquivo
```









