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

## Configurando Virtualenv para o Jupyter
https://janakiev.com/blog/jupyter-virtual-envs/

`pip install ipykernel`

`python -m ipykernel install --name=env`

`jupyter notebook`

![alt text](https://miro.medium.com/max/580/1*p2SCVuUuvRoJQS_zgd3Xnw.png)


## Configurando Extensoes para o Jupyter
https://towardsdatascience.com/jupyter-notebook-extensions-517fa69d2231

`pip install jupyter_contrib_nbextensions`

`jupyter contrib nbextension install`

## Extração do codigo no arquivo Jupyter.

`pip install nbconvert`

`jupyter nbconvert --to script *.ipynb`


## SonarQube

### Docker
`docker pull sonarqube`
`docker run -it --rm -p 9000:9000 -v '/${PWD}:/app' sonarqube`

https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/

### Linux
sonar-scanner \
  -Dsonar.projectKey=vision_test \
  -Dsonar.sources=. \
  -Dsonar.host.url=https://digital-sonarqube.eastus2.azurecontainer.io \
  -Dsonar.login=37cfe5cddaf4190b77206fea9461c8fa98edee3b

### Windows
sonar-scanner.bat -D"sonar.projectKey=vision_test" -D"sonar.sources=." -D"sonar.host.url=https://digital-sonarqube.eastus2.azurecontainer.io" -D"sonar.login=37cfe5cddaf4190b77206fea9461c8fa98edee3b"


## Sonarqube Docker
sonar-scanner.bat -D"sonar.projectKey=teste1" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.login=8cd57dad5624aa4123a32e09d3947e9a5d81b585"


sonar-scanner.bat -D"sonar.projectKey=dragon" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.login=9c977e64f7bbdebe2316fdc957613c1443ea1a80" 