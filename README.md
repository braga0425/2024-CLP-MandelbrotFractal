# Mandelbrot Project

This repository contains a project for visualizing the Mandelbrot Set using Python and a dynamic library (DLL) in C++ to compute the set's points. The project includes the necessary files to compile the DLL, as well as a Python script to generate and display the images.

## Repository Structure

- **clp/**
  - **mandelbrot/**
    - **mandelbrot.cpp**: C++ source code responsible for computing the Mandelbrot Set points;
    - **mandelbrot.sln**: Visual Studio solution file;
    - **x64/Release/**: Folder containing the compiled DLL `mandelbrot.dll`.
  - **gui.py**: Python script that uses the DLL to generate and display Mandelbrot Set images.

## Dependencies

To run the project, you will need the following Python packages:

- `numpy`;
- `Pillow`;
- `tkinter` (usually included in Python distributions).

Additionally, you will need **Make** to run the `make` commands.
These Python packages can be automatically installed using the command `make install-dependencies` (see the execution section below).

## Compiling the DLL

The `mandelbrot.dll` file is already available in the repository, so recompiling is not required to run the project. However, if you need or want to recompile the DLL, follow the steps below.

### How to Compile the DLL::

1. **Open Visual Studio and load the `mandelbrot.sln` project located in `clp/mandelbrot/`.
2. **Check the configuration**:
   - Ensure the configuration is set to `Release` and the platform to `x64`.
3. **Compile o projeto**:
   - From the top menu, click `Build` -> `Build Solution` (or press `Ctrl+Shift+B`);
   - This will generate the DLL in `clp/mandelbrot/x64/Release/mandelbrot.dll`.

## Running the Project

The `gui.py` script loads the DLL and uses the algorithm to generate Mandelbrot Set images. The script also provides a simple graphical interface to display the generated image.

### How to Run the Project:

1. **Install dependencies:**:

   - In the terminal, inside the `clp` folder, run:
  
     ```bash
     make install-dependencies
     ```

2. **Run the Python script:**:

   - To execute the script and generate the default image:
  
     ```bash
     make run
     ```

3. **Case Studies**:

   - The `Makefile` also provides three case studies with different parameters to generate distinct images:
     - Study 1 (Default wide view):
  
       ```bash
       make study1
       ```
       
     - Study 2 (Zoom on a branch):
  
       ```bash
       make study2
       ```
       
     - Study 3 (Extreme zoom on a specific feature):
  
       ```bash
       make study3
       ```

## Observações

- **Note**: The `mandelbrot.dll` file is already available in the repository and does not require recompilation to run the project. However, if you modify the C++ code or wish to compile it in a different environment, follow the instructions in the "Compiling the DLL" section.
- **Make on Windows**: If you are using Windows, ensure that `Make` is installed and available in the system path to use the `make` commands.
- The graphical interface uses `Tkinter`, which is included in most Python installations. If it is missing, you may need to install it separately.


# [PT-BR] Projeto Mandelbrot

Este repositório contém um projeto para a visualização do Conjunto de Mandelbrot usando Python e uma biblioteca dinâmica (DLL) em C++ para calcular os pontos do conjunto. O projeto inclui os arquivos necessários para compilar a DLL, além de um script Python para gerar e exibir as imagens.

## Estrutura do Repositório

- **clp/**
  - **mandelbrot/**
    - **mandelbrot.cpp**: Código-fonte em C++ responsável por calcular os pontos do Conjunto de Mandelbrot;
    - **mandelbrot.sln**: Arquivo de solução do Visual Studio;
    - **x64/Release/**: Pasta que contém a DLL compilada `mandelbrot.dll`.
  - **gui.py**: Script Python que utiliza a DLL para gerar imagens do Conjunto de Mandelbrot e exibi-las.

## Dependências

Para executar o projeto, você precisará dos seguintes pacotes Python:

- `numpy`;
- `Pillow`;
- `tkinter` (geralmente já incluído nas distribuições do Python).

Além disso, você precisará do **Make** para rodar os comandos `make`.
Esses pacotes Python podem ser instalados automaticamente usando o comando `make install-dependencies` (veja a seção de execução abaixo).

## Compilação da DLL

A DLL `mandelbrot.dll` já está disponível no repositório e não é necessário compilá-la novamente para executar o projeto. No entanto, se você precisar ou quiser recompilar a DLL, siga os passos abaixo.

### Como compilar a DLL:

1. **Abra o Visual Studio** e carregue o projeto `mandelbrot.sln` que se encontra em `clp/mandelbrot/`.
2. **Verifique a configuração**:
   - Certifique-se de que a configuração esteja definida para `Release` e a plataforma para `x64`.
3. **Compile o projeto**:
   - No menu superior, clique em `Build` -> `Build Solution` (ou pressione `Ctrl+Shift+B`);
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

## Observações

- **Atenção**: A DLL `mandelbrot.dll` já está disponível no repositório e não requer recompilação para a execução do projeto. Contudo, se você modificar o código C++ ou desejar compilar em um ambiente diferente, siga as instruções da seção "Compilação da DLL".
- **Make em Windows**: Se estiver usando Windows, certifique-se de que o `Make` está instalado e disponível no caminho do sistema para poder utilizar os comandos `make`.
- A interface gráfica usa `Tkinter`, que está incluída na maioria das instalações do Python. Se estiver faltando, você precisará instalá-la separadamente.
