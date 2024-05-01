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

1. Clone o repositório para sua máquina local:
   git@github.com:clsf/PBL1-REDES.git
2. Através
