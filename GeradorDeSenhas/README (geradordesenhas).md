# Gerador de Senhas

Este projeto é um gerador de senhas gráfico desenvolvido em Python usando a biblioteca Tkinter. Ele permite a criação de senhas seguras com diferentes tipos de caracteres, como letras maiúsculas, minúsculas, números e símbolos.
## Tecnologias Utilizadas

**Python** (Linguagem principal)

**Tkinter** (Biblioteca para interface gráfica)


## Funcionalidades

- Opção de selecionar o tipo de caracteres incluídos na senha.

- Definição do tamanho da senha entre 1 e 20 caracteres.

- Geração aleatória de senhas.

- Opção de copiar a senha gerada para a área de transferência.
## Como Executar o Projeto

Certifique-se de ter o Python instalado (versão 3.x).

Instale a biblioteca Pillow, se ainda não estiver instalada:

```bash
  pip install pillow
```
Baixe ou clone este repositório:

```bash
    git clone https://github.com/seu-usuario/gerador-de-senhas.git
    cd gerador-de-senhas
```
Execute o script principal:
```bash
 cd gerador-de-senhas
```
## Estrutura do código

**Importação de Bibliotecas**: Importa o Tkinter para a interface gráfica, a biblioteca Pillow para manipulação de imagens, além das bibliotecas string e random para a geração de senhas.

**Criação da Janela**: Configura a janela principal da aplicação.

**Funções**:

    - criar_senha(): Gera uma senha aleatória com base nos critérios selecionados pelo usuário.

    - copiar_senha(): Copia a senha gerada para a área de transferência e exibe uma mensagem de sucesso.

**Botões**: 

Botão gerar_senha: Dispara a função responsável por criar a senha.

Botão copiar_senha: Copia a senha gerada para a área de transferência.
## Contribuição

Se desejar contribuir com melhorias, sinta-se à vontade para enviar pull requests ou sugerir modificações na seção de issues do repositório.



## Licença

Este projeto é de uso livre e pode ser modificado conforme necessário.