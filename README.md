# deploy_API
simples API criada para auxiliar na agilidade de deploy, recebendo via Http todos os parâmetros necessários para funcionamento e persistindo em um banco de dados MySQL. 


Dockerfile e docker-compose incluso no projeto.

E possível acompanhar o andamento da aplicação através do arquivo de Log.

OBS: a API rodará na porta default 0.0.0.0:5000

## Como Usar

```docker-compose build```

```docker-compose up```


**Exemplo de chamada via curl**
 curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X POST  -d '{"componente": "testeaplicação", "versao":"1.2", "responsavel": "nobody", "status": "deployada"}' http://localhost:5000/api/deploy
  
  
  ## **EXTRA:**
  Para retorno dos dados no navegador, basta realizar a chamada da seguinte forma: 
  http://localhost:5000/api/deploy