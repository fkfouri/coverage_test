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

## Pytest-cov - https://pytest-cov.readthedocs.io/en/latest/
- rodando de forma normal: `pytest --cov=app`
- verbose: `pytest --cov=app -v`
- `pytest -v -o junit_family=xunit1 --cov=app --cov-report xml:test-results/coverage.xml --cov-report html:test-results/cov_html  --junitxml=test-results/results.xml` 

- `pytest -v -o junit_family=xunit1 --cov=app --cov-report xml:test-results/coverage.xml --junitxml=test-results/results.xml`


## SonarQube
`sonar-scanner.bat -D"sonar.projectKey=coverage" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.login=bba46f8771abfd98d8f1c2b4d1b2d33c3deecd6d"`

`sonar-scanner -X -D"project.settings=sonar-project.properties"`