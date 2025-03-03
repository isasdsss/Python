# Cronômetro em Tkinter

Este é um simples cronômetro desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica. Ele permite iniciar, pausar e reiniciar o cronômetro, além de mostrar o tempo no formato hh:mm:ss.

## Tecnologias Utilizadas

**Python** (Linguagem principal)

**Tkinter** (Biblioteca para interface gráfica)


## Funcionalidades

- **Iniciar**: Começa a contagem do cronômetro.

- **Pausar**: Pausa a contagem do cronômetro.

- **Reiniciar**: Reinicia o cronômetro para 00:00:00.
## Como Executar o Projeto

Certifique-se de ter o Python 3 instalado em sua máquina.

Clone este repositório ou baixe o código-fonte.

No terminal, navegue até o diretório do projeto.

Execute o seguinte comando:

```bash
  python cronometro.py
```
    
## Estrutura do código

**Importação de Bibliotecas**: Importa o Tkinter e define cores personalizadas.

**Criação da Janela**: Configura a janela principal da aplicação.

**Variáveis**: Define variáveis globais para armazenar o tempo, o estado do cronômetro e o contador.

    -   tempo = '00:00:00'
        rodar = False
        contador = -5
        limitador = 59

**Funções**:

    - iniciar(): Inicia o cronômetro e atualiza o tempo na interface gráfica. Contabiliza os segundos, minutos e horas.

    - start(): Ativa o cronômetro quando clicado no botão "Iniciar".

    - pausar(): Pausa o cronômetro quando clicado no botão "Pausar"

    - reiniciar(): Reinicia o cronômetro para o valor 00:00:00 quando clicado no botão "Reiniciar".

**Botões**: Configura os botões para iniciar, pausar e reiniciar o cronômetro, com o texto e as posições na interface gráfica.
## Contribuição

Se desejar contribuir com melhorias, sinta-se à vontade para enviar pull requests ou sugerir modificações na seção de issues do repositório.



## Licença

Este projeto é de uso livre e pode ser modificado conforme necessário.