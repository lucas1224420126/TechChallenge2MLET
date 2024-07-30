# Extração de Dados Embrapa

Este projeto realiza a extração de dados da Embrapa utilizando o FastAPI, conectando-se diretamente ao site da Embrapa [VitiBrasil](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01). O usuário pode extrair dados de produção, processamento, comercialização, importação e exportação. Os dados são retornados em formato CSV.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Autenticação](#autenticação)
- [Consultas Disponíveis](#consultas-disponíveis)
- [Licença](#licença)
- [Contato](#contato)

## Instalação

Para configurar o ambiente de desenvolvimento e instalar todas as dependências necessárias, siga os passos abaixo:

1. É Necessario ter o docker instalado, caso não basta ir no site https://www.docker.com/.

2. Clone este repositório:

    ```bash
    git clone https://github.com/seu_usuario/seu_projeto.git
    ```

3. Entre no diretório do projeto:

    ```bash
    cd seu_projeto
    ```

4. Para rodar o projeto basta executar o comando:

    ```bash
    docker-compose up -d
    ```
5. Caso precise remover o container é so executar o comando `docker-compose down`


## Desenvolvimento via container

Caso queria trabalhar dentro do container docker sem precisar instalar nada na maquina basta seguir os passos abaixo:

1. Instalar a extenção `Dev Containers``
2. Clicar em anexar janela atual ou clicar no icone `->`
3. Em seguida vai abrir uma caixa é so navegar ate `/usr/src/techchallenge2mlet`, e clicar em ok





Com base nas informações fornecidas, aqui está um modelo de README para o seu projeto de extração de dados da Embrapa utilizando o FastAPI:

```markdown
# Extração de Dados Embrapa

Este projeto realiza a extração de dados da Embrapa utilizando o FastAPI, conectando-se diretamente ao site da Embrapa [VitiBrasil](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01). O usuário pode extrair dados de produção, processamento, comercialização, importação e exportação. Os dados são retornados em formato CSV.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Autenticação](#autenticação)
- [Consultas Disponíveis](#consultas-disponíveis)
- [Licença](#licença)
- [Contato](#contato)

## Instalação

Para configurar o ambiente de desenvolvimento e instalar todas as dependências necessárias, siga os passos abaixo:

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu_usuario/seu_projeto.git
    ```

2. Entre no diretório do projeto:

    ```bash
    cd seu_projeto
    ```

3. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para executar o FastAPI, utilize o seguinte comando dentro do seu ambiente virtual:

```bash
uvicorn app.main:app --reload
```

Certifique-se de estar na pasta correta ao executar o comando. Após iniciar, você verá uma mensagem de sucesso e poderá acessar a documentação da API em:

[http://127.0.0.1/docs](http://127.0.0.1/docs)

## Autenticação

Estamos utilizando um método de autenticação, então será necessário validar-se para realizar as consultas.

1. Na documentação da API, clique na opção `auth`.
2. Insira qualquer nome de usuário e senha que você se lembre e clique em "Execute".
3. Armazene o `access_token` e o `token_type` retornados.
4. No topo da página, clique no botão verde `Authorize`.
5. Insira o `username`, `password`, e as informações de token armazenadas, depois clique em "Authorize".

## Consultas Disponíveis

### Consulta de Produção

Retorna os dados de produção de vinhos, sucos e derivados do Rio Grande do Sul.

### Consulta de Processamento

Retorna dados de quantidade de uvas processadas no Rio Grande do Sul, incluindo variedades viníferas, americanas, híbridas, uvas de mesa e sem classificação.

### Consulta de Comercialização

Retorna dados de comercialização de vinhos e derivados no Rio Grande do Sul.

### Consulta de Importação

Retorna dados de importação de derivados de uva, incluindo vinhos de mesa, espumantes, uvas frescas, uvas passas e sucos de uva.

### Consulta de Exportação

Retorna dados de exportação de derivados de uva, incluindo vinhos de mesa, espumantes, uvas frescas e sucos de uva.

## Licença

Este projeto está licenciado sob a licença XYZ - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
