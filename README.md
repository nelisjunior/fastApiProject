# FASTAPI PROJECT

Projeto baseado em: <https://github.com/digitalinnovationone/workout_api>
Repositório dos testes via Postman: <https://documenter.getpostman.com/view/23096957/2sA2rDxM8P>

## Preparando o ambiente de desenvolvimento

### No windows

1. Instalação do Python
 Versão Python adotada: [3.11.4](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe)

- Baixar e instalar o Python
- Verificar a instalação com o comando `python --version`
- Verificar a instalação com o comando `pip --version`
- Atualizar o pip com o comando `python -m pip install --upgrade pip`
- Verificar a instalação com o comando `pip --version`

2. Instale e configure o MakeFile
   - Usando o Chocolatey, usando um terminal com permissões de administrador, execute o comando `choco install make`
   - Verifique a instalação com o comando `make --version`

3. Instalação do ambiente virtual
4. 

> O ambiente virtual adotado é o virtualenv

- Instalar o virtualenv com o comando `pip install virtualenv`
- Verificar a instalação com o comando `virtualenv --version`
- Criar um ambiente virtual com o comando `virtualenv env_{nome_do_ambiente}`
- Ativar o ambiente virtual com o comando `env_{nome_do_ambiente}\Scripts\activate`
  - Desativar o ambiente virtual com o comando `deactivate`

4. Instalação dos pacotes

- Instalar o pacote fastapi com o comando `pip install fastapi uvicorn sqlalchemy pydantic`

5. Iniciando o servidor

- Executar o comando `uvicorn workout_api.main:app --reload`

## Desafio


- [x] Adicionar query parameters nos endpoints
    - [x] Atleta
        - [x] Nome
        - [x] CPF
- [x] Customizar response de retorno de endpoints
    - [x] Get all
        - [x] Atleta
            - [x] Nome
            - [x] Centro de treinamento
            - [x] Categoria
- [ ] Manipular exceção de integridade dos dados em cada módulo/tabela
    - [ ] Tratar sqlalchemy.exc.IntegrityError e devolver a seguinte mensagem: “Já existe um atleta cadastrado com o cpf: x”
    - [ ] Definir status_code: 303
- [ ] Adicionar paginação utilizando a lib: fastapi-pagination
    - [ ] Implementar limit e offset

