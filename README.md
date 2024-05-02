# Problema 1: Internet das coisas

Este projeto é uma solução para o problema 1 do PBL de Concorrência e Conectividade que consiste em três componentes principais: um dispositivo em Python, um broker em Python e uma aplicação em Java. O dispositivo envia mensagens para o broker, que encaminha para a aplicação para processamento, assim como a aplicação envia requisições ao dispositivo através do broker.

## Sumário
- [Introdução](#introdução)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Introdução
No presente projeto demonstra a comunicação entre o dispositivo, que possui algumas funcionalidades como modificação de velocidade e consumo (que varia com o tempo), e a aplicação que serve como interface para o usuário. Essa comunicação se dá através do serviço broker. O broker recebe as requisições, tanto do dispositivo, quanto da aplicação, e faz os devidos encaminhamentos das mensagens. 

## Instalação
Para instalar o projeto, siga estas instruções:

### 1. Clone o repositório para sua máquina local:
      git@github.com:clsf/PBL1-REDES.git
### 2. Para utilizar o dispositivo e o broker através do docker, realizar o seguinte comando:
#### 2.1 Inicializando o broker:
      docker pull claudiainees/my_images:broker-01
      docker run --network=host -d -p 5433:5433 claudiainees/my_images:broker-01
#### 2.2 Inicializando o dispositivo:
      docker pull claudiainees/my_images:device-01
      docker run --network=host -d -p 5432:5432 claudiainees/my_images:device-01

##### Se estiver rodando o broker e o device em máquinas diferentes, precisará informar o IP do broker ao utilizar o comando docker run:
       docker run --network=host -e BROKER_ADDRESS=IP_DO_BROKER -d -p 5432:5432 claudiainees/my_images:device-01

### 3. Iniciando a aplicação:
Para inicializar a aplicação utilize uma IDE de sua preferência, recomendo a IDE IntelliJ IDEA. Com a IDE abra a pasta da  [aplicação](./Aplicacao).

