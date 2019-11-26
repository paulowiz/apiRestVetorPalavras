## 📚  Descrição 

API que gera dois tipos de vocabulário referente a um conjunto de textos.

## 📌Endpoints:

Foram criados quatro endpoints do tipo POST no qual todos eles ao receber um conjunto de textos irão ter seus respectivos retornos.

### /getLogs

Retorna os logs de requisições em um banco hospedado na nuvem.

![image](https://user-images.githubusercontent.com/18649504/69592388-7fcf5900-0fd4-11ea-9280-71d3c734e8dc.png)

### /geraVetoresIsolados 

Gera os vetores isolados dos textos que foram enviados

![image](https://user-images.githubusercontent.com/18649504/69520917-9629d600-0f3c-11ea-8af4-6aa3d40a1722.png)

### /geraVocabularioIsolado

Gera o vocabulário isolado dos textos que foram enviados sem as "Stop-Words"

![image](https://user-images.githubusercontent.com/18649504/69521098-f751a980-0f3c-11ea-94c4-da3922fd3476.png)


### /geraVetoresDuplos

Gera os vetores duplos (2-gram) dos textos que foram enviados

![image](https://user-images.githubusercontent.com/18649504/69521128-0a647980-0f3d-11ea-9752-1a91e897814f.png)


### /geraVocabularioDuplo

Gera o vocabulario duplo (2-gram) dos textos que foram enviados

![image](https://user-images.githubusercontent.com/18649504/69521208-354ecd80-0f3d-11ea-916b-576ddbd90b75.png)

## 🚀 Tecnologias Usadas 

<img src="https://user-images.githubusercontent.com/18649504/66262823-725cd600-e7be-11e9-9cea-ea14305079db.png" width = "100">

<img src="https://user-images.githubusercontent.com/18649504/69592604-2ae01280-0fd5-11ea-827f-00963982ea74.png" width = "100">

## Estrutura do Projeto 📌
 |-- controller
    |-- functions.py
 |-- database
     |-- conexao.py
 |-- config.ini
 |-- main.py
 |-- requiriments.txt

## 📢 Como executar

Requisitos:

Python 3.7.4<br>

Instalar todas as depedências do python usando o arquivo requiriments.txt que está no projeto:  

```bash 
pip install  -r requiriments.txt
 ```  
 Executar o main.py no cmd com o comando:

```bash 
python main.py
 ```  
Para efetuar o teste você precisa somente utilizar algum programa que consiga fazer um post na API REST( Recomendo o Postman que de sugestão já deixei a collection dentro do arquivo do projeto).

```bash 
Api_Vocabulario.postman_collection.json
 ```  
e informar o IP: http://127.0.0.1:5000/+endpoint , preenchendo o body no formato JSON conforme abaixo:

![image](https://user-images.githubusercontent.com/18649504/69520429-7645e280-0f3b-11ea-988d-0b5bb5fd69c7.png)


## 🔓 Licença 
MIT © [Paulo Mota](https://www.linkedin.com/in/paulo-mota-955218a2/)
