## Configuração de Ambiente Virtual

1 - Instalando o ambiente virtual Python

`pip install virtualenv`

2 - Criando o ambiente virtual chamando 'env'.

`python -m venv env`

2 - Habilitando o ambiente virtual

`.\env\Scripts\activate`

3 - Atualizar pip
`python -m pip install --upgrade pip`

## Instalando os pacotes a partir do requirement file

`pip install -r requirements.txt`

## Pytest
`pytest`

## Coverage
- `coverage run app.py`
- `coverage report`
- mostrando missing `coverage report -m` ou `coverage report --show-missing`
- exibindo formato html `coverage html`

## Pytest-cov
