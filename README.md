# Problema 1: Internet das coisas

Este projeto é uma solução para o problema 1 do PBL de Concorrência e Conectividade que consiste em três componentes principais: um dispositivo em Python, um broker em Python e uma aplicação em Java. O dispositivo envia mensagens para o broker, que encaminha para a aplicação para processamento, assim como a aplicação envia requisições ao dispositivo através do broker.

## Sumário
- [Introdução](#introdução)
- [Iniciando a Aplicação](#iniciando-a-aplicação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)


## Introdução
No presente projeto demonstra a comunicação entre o dispositivo, que possui algumas funcionalidades como modificação de velocidade e consumo (que varia com o tempo), e a aplicação que serve como interface para o usuário. Essa comunicação se dá através do serviço broker. O broker recebe as requisições, tanto do dispositivo, quanto da aplicação, e faz os devidos encaminhamentos das mensagens. 

## Iniciando a aplicação
É possível iniciar a aplicação de duas formas, uma delas é através dos arquivos e a outra é utilizando imagens docker:

### 1. Inicializando o projeto através dos arquivos:
A inicialização através dos arquivos só é recomendada para a utilização do broker, dispositivo e aplicação na mesma máquina.
#### 1.1 Clone o repositório para sua máquina local:
      git@github.com:clsf/PBL1-REDES.git
      
#### 1.2 Inicializando o broker:
Para utilização do broker e do dispositivo, é necessário que tenha o Python3 instalado na sua máquina, navegue até a pasta do [broker](./broker). Após abrir a pasta do broker, abra o terminal dentro da pasta e digite o seguinte comando:

      python3 mainBroker.py
      
Após o comando, o broker será inicializado no terminal.

#### 1.3 Inicializando o dispositivo:
Navegue até a pasta do [dispositivo](./dispositivo), abra o terminal dentro da pasta e digite o seguinte comando:

      python3 mainDevice.py
      
Após o comando, o dispositivo será inicializado no terminal.

#### 1.4 Inicializando a aplicação:
Para inicializar a aplicação utilize uma IDE que execute programas em JAVA de sua preferência, recomendo a IDE IntelliJ IDEA. Com a IDE abra a pasta da  [aplicação](./Aplicacao).
Caso esteja rodando o broker e o dispositivo na mesma máquina, não será necessário configurações adicionais. 

### 2. Inicializando o projeto através do docker:
#### 2.1 Inicializando o broker:

      docker pull claudiainees/my_images:broker-03
      
Se estiver rodando aplicação, broker e dispositivo na mesma máquina: 

      docker run -it --network=host claudiainees/my_images:broker-03
      
Se precisar definir as portas que o broker utilizará, use o seguinte comando:

      docker run -it --network=host -e PORT_TO_DEVICE=PORTA_ESCOLHIDA_DEVICE -e PORT_TO_APP=PORTA_ESCOLHIDA_APP claudiainees/my_images:broker-03
      
Substitua PORTA_ESCOLHIDA_DEVICE e PORTA_ESCOLHIDA_APP pelas portas que deseja utilizar.
#### 2.2 Inicializando o dispositivo:

      docker pull claudiainees/my_images:device-02
      
Se estiver rodando broker e dispositivo na mesma máquina:

      docker run -it --network=host claudiainees/my_images:device-02

Se precisar definir as portas que o dispositivo utilizará, ou se estiver definido uma porta para o broker, ou mesmo rodando o broker e dispositivo em computadores diferentes,utilize o seguinte comando:

      docker run -it --network=host -e BROKER_ADDRESS=IP_DO_BROKER -e BROKER_PORT=PORTA_DO_BROKER -e PORT=PORTA_DISPOSITIVO -e DEVICE_NAME=VENTILADOR claudiainees/my_images:device-02

A variável "BROKER_ADDRESS" precisa receber o IP da máquina que o broker está rodando, "BROKER_PORT" a porta que o broker está funcionando, anteriormente definida como "PORT_TO_DEVICE" na inicialização do broker. A variável "PORT" recebe a porta que o dispositivo utilizará para realizar a comunicação e "DEVICE_NAME" o nome que deseja dar para o dispositivo.

#### 2.3 Inicializando a aplicação:

      docker pull claudiainees/my_images:app-image-01

Se estiver rodando a aplicação na mesma máquina que o broker e não tiver feito alterações da porta dele, utilize o seguinte comando:

      docker run -it --network=host claudiainees/my_images:app-image-01

Caso esteja em máquinas diferentes, e/ou tenha alterado a porta de excecução do broker "PORT_TO_APP", utilize o seguinte comando:

      docker run -it --network=host -e FEIGN_CLIENT_CONFIG_BROKER_URL=http://IPDOBROKER:PORTADOBROKER -e SERVER_PORT=8085 claudiainees/my_images:app-image-01

Altere o "IPDOBROKER" e "PORTADOBROKER" pelo ip e porta do broker. É possível também alterar a porta que a aplicação irá rodar, foi utilizado 8085 na chamada do comando, mas pode alterar para a porta que achar melhor. 

## Uso
Para utilizar a rede de comunicação é necessário ter realizado o passo de [Iniciando a Aplicação](#iniciando-a-aplicação). No terminal da aplicação será exibida as opções da Figura 1. Ao inicializar a aplicação, não terá dispositivos disponíveis, logo será preciso selecionar a opção Buscar Dispositivos.
<a name="tela Inicial"></a>
<div align="center">
  <img src="/img/telaInicial.png" alt="" width="350">
   <p>
      Figura 1: Tela Inicial.
    </p>
</div>

Ao selecionar "Buscar Dispositivos" será exibida uma lista de dispositivos disponíveis. Após isso, selecionar o dispositivo de acordo com a numeração, como na Figura 2.

<a name="Selecionando device"></a>
<div align="center">
  <img src="/img/selecionandoDevice.png" alt="" width="350">
   <p>
      Figura 2: Selecionando o dispositivo.
    </p>
</div>

Quando o dispositivo for selecionado, informações sobre ele serão exibidas como na Figura 3. Inicialmente ele estará desligado, mas pode mudar o estado usando a opção "Alterar a velocidade" e passando a velocidade desejada (Figura 4).
<a name="Device"></a>
<div align="center">
  <img src="/img/Device.png" alt="" width="350">
   <p>
      Figura 3: Informações do dispositivo.
    </p>
</div>

<a name="Alterando velocidade"></a>
<div align="center">
  <img src="/img/alterandoVelocidade.png" alt="" width="350">
   <p>
      Figura 4: Alterando a velocidade do dispositivo.
    </p>
</div>

O consumo do dispositivo é alterado com o tempo, é possível verificar o novo consumo ou o estado mais recente do dispositivo selecionando a opção atualizar.
<a name="estado atual"></a>
<div align="center">
  <img src="/img/estadoAtual.png" alt="" width="350">
   <p>
      Figura 5: Estado atual do dispositivo.
    </p>
</div>

## Estrutura do Projeto
O projeto possui a seguinte estrutura:
- Broker: Código para o broker em Python.
- Dispositivo: Código para o dispositivo em Python.
- Aplicação: Código para a aplicação em Java.
