# Backend Project Rush
Este é o README para o projeto Backend Project Rush. Aqui você encontrará instruções sobre como rodar o projeto, configurar o ambiente e as rotas disponíveis.

## Como Rodar o Projeto

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/backend-project-rush.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd backend-project-rush
    ```
3. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
5. Aplique as migrações do banco de dados:
    ```sh
    python manage.py migrate
    ```
6. Inicie o servidor:
    ```sh
    python manage.py runserver
    ```

## Configuração do Ambiente

1. Crie um arquivo `.env` na raiz do projeto, verique o arquivo `.env.example`.
2. Gere uma SECRET_KEY como o comando:
    ```sh
    python utils/gen_secret_key.py
    ```
3. Adicione as seguintes variáveis de ambiente ao arquivo `.env`:
    ```env
    DEBUG=True
    SECRET_KEY=sua-chave-secreta-gerada
    ```

## Rotas Disponíveis

As rotas disponíveis para este projeto estão documentadas no Swagger. Para acessar a documentação das rotas, inicie o servidor e navegue até o seguinte endereço no seu navegador:

```
http://localhost:8000/swagger/
```

Aqui você encontrará uma interface interativa onde poderá visualizar e testar todas as rotas da API.
