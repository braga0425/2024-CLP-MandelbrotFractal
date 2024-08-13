# Mandelbrot Set Visualization

Este repositório contém um projeto para a visualização do Conjunto de Mandelbrot usando Python e uma biblioteca dinâmica (DLL) em C++ para calcular os pontos do conjunto. O projeto inclui os arquivos necessários para compilar a DLL, além de um script Python para gerar e exibir as imagens.

## Estrutura do Repositório

- **clp/**
  - **mandelbrot/**
    - **mandelbrot.cpp**: Código-fonte em C++ responsável por calcular os pontos do Conjunto de Mandelbrot.
    - **mandelbrot.sln**: Arquivo de solução do Visual Studio.
    - **x64/Release/**: Pasta que contém a DLL compilada `mandelbrot.dll`.
  - **gui.py**: Script Python que utiliza a DLL para gerar imagens do Conjunto de Mandelbrot e exibi-las.

## Dependências

Para executar o projeto, você precisará dos seguintes pacotes Python:

- `numpy`
- `Pillow`
- `tkinter` (geralmente já incluído nas distribuições do Python)

Além disso, você precisará do **Make** para rodar os comandos `make`.
Esses pacotes Python podem ser instalados automaticamente usando o comando `make install-dependencies` (veja a seção de execução abaixo).

## Compilação da DLL

A DLL `mandelbrot.dll` já está disponível no repositório e não é necessário compilá-la novamente para executar o projeto. No entanto, se você precisar ou quiser recompilar a DLL, siga os passos abaixo.

### Como compilar a DLL:

1. **Abra o Visual Studio** e carregue o projeto `mandelbrot.sln` que se encontra em `clp/mandelbrot/`.
2. **Verifique a configuração**:
   - Certifique-se de que a configuração esteja definida para `Release` e a plataforma para `x64`.
3. **Compile o projeto**:
   - No menu superior, clique em `Build` -> `Build Solution` (ou pressione `Ctrl+Shift+B`).
   - Isso gerará a DLL em `clp/mandelbrot/x64/Release/mandelbrot.dll`.

## Execução do Projeto

O script `gui.py` carrega a DLL e utiliza o algoritmo para gerar imagens do Conjunto de Mandelbrot. O script também fornece uma interface gráfica simples para exibir a imagem gerada.

### Como executar o projeto:

1. **Instale as dependências**:

   - No terminal, dentro da pasta `clp`, execute:
     ```bash
     make install-dependencies
     ```

2. **Execute o script Python**:

   - Para rodar o script e gerar a imagem padrão:
     ```bash
     make run
     ```

3. **Casos de Estudo**:

   - O `Makefile` também fornece três casos de estudo com diferentes parâmetros para gerar imagens distintas:
     - Estudo 1 (Visão ampla padrão):
       ```bash
       make study1
       ```
     - Estudo 2 (Zoom em uma ramificação):
       ```bash
       make study2
       ```
     - Estudo 3 (Zoom extremo em uma característica específica):
       ```bash
       make study3
       ```

4. **Limpeza**:
   - Não há arquivos temporários a serem limpos, mas você pode executar:
     ```bash
     make clean
     ```

## Observações

- **Atenção**: A DLL `mandelbrot.dll` já está disponível no repositório e não requer recompilação para a execução do projeto. Contudo, se você modificar o código C++ ou desejar compilar em um ambiente diferente, siga as instruções da seção "Compilação da DLL".
- **Make em Windows**: Se estiver usando Windows, certifique-se de que o `Make` está instalado e disponível no caminho do sistema para poder utilizar os comandos `make`.
- A interface gráfica usa `Tkinter`, que está incluída na maioria das instalações do Python. Se estiver faltando, você precisará instalá-la separadamente.
