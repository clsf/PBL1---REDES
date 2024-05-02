# Use uma imagem base com Maven para compilar o projeto
FROM maven:3.8.4-openjdk-11 AS build

# Defina o diretório de trabalho
WORKDIR /app

# Copie o `pom.xml` para o contêiner
COPY pom.xml .

# Baixe as dependências Maven (isso será armazenado em cache se o `pom.xml` não mudar)
RUN mvn dependency:go-offline

# Copie o restante do projeto para o contêiner
COPY . .

# Compile o projeto (gera o arquivo .jar no diretório `target`)
RUN mvn clean package

# Use uma imagem base do OpenJDK para executar a aplicação
FROM openjdk:11-jre-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo .jar do estágio de build para o contêiner
COPY --from=build /app/target/nome-do-projeto-1.0.jar .

# Defina o comando para iniciar a aplicação
CMD ["java", "-jar", "demo-0.0.1-SNAPSHOT.jar"]
