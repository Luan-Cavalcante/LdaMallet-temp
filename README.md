# LdaMallet-temp

# RESEARCH

## Pesquisa sobre o uso do LdaMallet

### Descrição

O objetivo da pesquisa é conseguir combinar o uso do LdaMallet,a implementação com wrappers do gensim, com dados de teste para começar a comparar resultados com o objetivo de possivelmente adotar essa abordagem no laboratório.

### Instalação

É preciso ter Java instalado, **não se tem informações sobre a versão do Java** :

    sudo apt-get install openjdk-11-jdk
    
Para verificar se foi instalado corretamente :

    java -version
    
Se aparecer algo parecido com, tudo está certo :
```
openjdk version "11.0.15" 2022-04-19
OpenJDK Runtime Environment (build 11.0.15+10-Ubuntu-0ubuntu0.20.04.1)
OpenJDK 64-Bit Server VM (build 11.0.15+10-Ubuntu-0ubuntu0.20.04.1, mixed mode, sharing)

```
Próximo passo :

    sudo apt install ant
    

**IMPORTANTE** 

É necessário saber a path em que o Mallet é clonado, pois ela será necessária no código.

      git clone https://github.com/mimno/Mallet.git
      
Vá para a pasta Mallet:

    cd Mallet
    
E dê o comando : 
      
    ant

Se acabar com BUILD SUCCESSFUL, great job ! Tá pronto para o uso !

# Tutorial de Instalação 

Para fazer uso do LdaMallet, cujo documentação de instalação se encontra em : https://mallet.cs.umass.edu/download.php, que é uma implementação em Java de LDA, é preciso ter java instalado na máquina. Mas para facilitar nosso progresso na linguagem Python.O Gensim fornece um wrapper, que faz uso do LdaMallet em Java. A documentação desse wrapper se encontra em : https://radimrehurek.com/gensim_3.8.3/models/wrappers/ldamallet.html.

Para usar o wrapper do Gensim, é necessário que a versão 3.8.3 seja utilizada. Para isso será utilizado ambientes virtuais, pois é necessário usar especificamente essa versão. O tutorial utilizado foi : https://anbasile.github.io/posts/2017-06-25-jupyter-venv/.

Todo o passo a passo será feito aqui.

## Set do ambiente virtual e kernel.

Como a ferramenta utilizada para rodar os notebooks é o Jupyter Lab, é necessário criar um ambiente virtual e depois criar um kernel com as especificações de versões que serão utilizadas. 

    
    python3 -m venv nomedovenv
    
Ative o ambiente :

    source nomedovenv/bin/activate
    
Agora de dentro do ambiente virtual : 
    
    pip install ipykernel
    
 Dê mais o comando : 
 
    ipython kernel install --user --name=projectname
    

## Requirements

Agora com os ambiente virtual e com o kernel criado, é preciso instalar aquilo que será utilizado.


```
pip install -r requirements.txt
```

## Kernel 

Agora selecione o kernel criado clicando no kernel selecionado no canto superior esquerdo que provavelmente será python3 e escolha o que você criou.

Para verificar se a versão do Gensim instalada é a certa, dê um :

    pip freeze 
    
E procure por gensim==3.8.3, se achar, tudo certo.

## LdaMallet

É necessário saber onde a instalação do LdaMallet foi feita, pois a path com o mallet binário é utilizada.
Sendo assim, tenha ciência de onde ela foi criada e quando achar use o comando :
    
    pwd
    
copie a path e cole na linha XX do código. 

## Boa sorte !

### Authors and acknowledgment
O Lda Mallet foi apresentado em um TDD pelo Professor Thiago de Paulo. E também foi utilizada uma classe criada pelo mesmo, utilizada no processo para gerar nossos testes.

### License
For open source projects, say how it is licensed.
