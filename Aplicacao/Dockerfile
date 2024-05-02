# Use uma imagem base com Maven para compilar o projeto
FROM maven:3.8.8-eclipse-temurin-17 AS builder

# Defina o diretório de trabalho
WORKDIR /app

# Copie o `pom.xml` para o contêiner
COPY pom.xml .

# Baixe as dependências Maven (armazenado em cache se o `pom.xml` não mudar)
RUN mvn dependency:go-offline

# Copie o restante do projeto para o contêiner
COPY . .

# Compile o projeto (gera o arquivo .jar no diretório `target`)
RUN mvn clean package

# Use uma imagem base do OpenJDK para executar a aplicação
FROM eclipse-temurin:17

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo .jar do estágio de build para o contêiner final
COPY --from=builder /app/target/demo-0.0.1-SNAPSHOT.jar /app/

# Defina o comando para iniciar a aplicação
CMD ["java", "-jar", "/app/demo-0.0.1-SNAPSHOT.jar"]
