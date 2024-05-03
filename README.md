# Problema 1: Internet das coisas

Este projeto é uma solução para o problema 1 do PBL de Concorrência e Conectividade que consiste em três componentes principais: um dispositivo em Python, um broker em Python e uma aplicação em Java. O dispositivo envia mensagens para o broker, que encaminha para a aplicação para processamento, assim como a aplicação envia requisições ao dispositivo através do broker.

## Sumário
- [Introdução](#introdução)
- [Instalação e configuração](#instalação-e-configuração)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)


## Introdução
No presente projeto demonstra a comunicação entre o dispositivo, que possui algumas funcionalidades como modificação de velocidade e consumo (que varia com o tempo), e a aplicação que serve como interface para o usuário. Essa comunicação se dá através do serviço broker. O broker recebe as requisições, tanto do dispositivo, quanto da aplicação, e faz os devidos encaminhamentos das mensagens. 

## Instalação e configuração
Para instalar o projeto, siga estas instruções:

### 1. Clone o repositório para sua máquina local:
      git@github.com:clsf/PBL1-REDES.git
### 2. Para utilizar o dispositivo e o broker através do docker, realizar o seguinte comando:
#### 2.1 Inicializando o broker:
      docker pull claudiainees/my_images:broker-03
      docker run --network=host -d -p 5433:5433 claudiainees/my_images:broker-03
Caso queira definir qual será a porta que irá rodar o broker utilize o seguinte comando:

      docker run --network=host -e PORT_TO_DEVICE=5433 -e PORT_TO_APP=5000 claudiainees/my_images:broker-03 
Substitua pelas portas que deseja utilizar.
#### 2.2 Inicializando o dispositivo:
      docker pull claudiainees/my_images:device-02
      docker run --network=host -d -p 5432:5432 claudiainees/my_images:device-02

##### Se estiver rodando o broker e o device em máquinas diferentes, precisará informar o IP do broker ao utilizar o comando docker run:
       docker run --network=host -e BROKER_ADDRESS=IP_DO_BROKER -d -p 5432:5432 claudiainees/my_images:device-02
Caso tenha alterado a porta do broker utilize o seguinte comando para inicializar passando o IP e a Porta do broker:

      docker run --network=host -e BROKER_ADDRESS=IP_DO_BROKER -e BROKER_PORT:SUBSTITUA_PELA_PORTA -d -p 5432:5432 claudiainees/my_images:device-02
### 3. Iniciando a aplicação:
Para inicializar a aplicação utilize uma IDE de sua preferência, recomendo a IDE IntelliJ IDEA. Com a IDE abra a pasta da  [aplicação](./Aplicacao).
Caso esteja rodando o broker e o dispositivo na mesma máquina, não será necessário configurações adicionais. Caso a aplicação esteja em uma máquina distinta ao broker, será necessário configurar o IP do broker no [application](./Aplicacao/src/main/resources/application.yml). Substitua url: http://localhost:5000 pelo IP e porta do broker: http://IP:PORTA.

Por fim,  inicialize utilizando o arquivo [DemoApplication](./Aplicacao/src/main/java/com/testefront/demo/DemoApplication.java). 
#### 3.1 Inicializando a aplicação com docker:
       docker pull claudiainees/my_images:app-image-01
       docker run -it --network=host claudiainees/my_images:app-image-01
Caso precise definir a porta do broker, por estar em outra máquina execute o seguinte comando para inicializar:

       docker run -it --network=host -e FEIGN_CLIENT_CONFIG_BROKER_URL=http://IPDOBROKER:PORTADOBROKER claudiainees/my_images:app-image-01
## Uso
Para utilizar a rede de comunicação é necessário ter realizado o passo de [Instalação e configuração](#instalação-e-configuração). No terminal da aplicação será exibida as opções da Figura 1. Ao inicializar a aplicação, não terá dispositivos disponíveis, logo será preciso selecionar a opção Buscar Dispositivos.
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
