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

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

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
