# Backend Project Rush
Este é o README para o projeto Backend Project Rush. Aqui você encontrará instruções sobre como rodar o projeto, configurar o ambiente e as rotas disponíveis.

## Configuração do Ambiente

1. Crie um arquivo `.env` na raiz do projeto, verique o arquivo `.env.example`.
2. Gere uma SECRET_KEY como o comando:
    ```sh
    python3 utils/gen_secret_key.py
    ```
3. Adicione as seguintes variáveis de ambiente ao arquivo `.env`:
    ```env
    DEBUG="True"
    SECRET_KEY="sua-chave-secreta-gerada"
    ```

## Como Rodar o projeto

1. Crie e ative um ambiente virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
2. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
3. Crie as migrações pendentes:
    ```sh
    python manage.py makemigrations api
    ```
4. Aplique as migrações do banco de dados:
    ```sh
    python manage.py migrate
    ```
5. Inicie o servidor:
    ```sh
    python manage.py runserver
    ```

## Rotas Disponíveis

As rotas disponíveis para este projeto estão documentadas no Swagger. Para acessar a documentação das rotas, inicie o servidor e navegue até o seguinte endereço no seu navegador:

```
http://localhost:8000/swagger/
```

Aqui você encontrará uma interface interativa onde poderá visualizar e testar todas as rotas da API.
