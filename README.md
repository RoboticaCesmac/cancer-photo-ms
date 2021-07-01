<h1> API - Avaliação Cancer Bucal</h1>

- Microserviço criado com Flask e Docker para avaliação de cancer bucal. 

<h2>Instrução</h2>

<p>Adicione o seu modelo criado com o Keras na pasta <b>modelo-treinado</b>. Um modelo de teste pode ser encontrado no link: <a href="http://cwg.services/cesmac/cancer-bucal/modelo-treinado.tar">Modelo Reconhecimento - Elefante e Girafa</a></p>

<p>Enviar o campo image via POST para <b>/image</b></p>

<p>O campo image pode ser:</p>

- URL para uma imagem na internet
- Imagem no formato de Base64

<p>O retorno da aplicação será um JSON contendo</p>

```
{
    "value":"0",
    "value_name": "Não possui câncer",
    "acc": "0.9999"
}
```

| Campo      | Valor                                        | Descrição                                |
|------------|----------------------------------------------|------------------------------------------|
| value      | 0 ou 1                                       | 0 = Não possui cancer / 1 = pode possuir |
| value_name | "pode possuir câncer" ou "não possui câncer" |                                          |
| acc        | valor entre 0-1                              | Probabilidade (Acurácia 0 - 1)           |
-----------------------
<h2>Executando</h2>

<p>Executar no terminar</p>
```
docker compose up -d
```

----------------------
<p><b>Autor:</b> Carlos W. Gama(@carloswgama)</p>