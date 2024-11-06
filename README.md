
# YouTube Video Downloader

Este é um Projeto em Python simples para baixar vídeos do YouTube com uma interface gráfica usando as bibliotecas Tkinter e yt-dlp. O script permite a inserção de uma URL do YouTube, seleção do diretório de destino e escolha da qualidade e formato do vídeo desejado.


## Funcionalidades

- Interface gráfica construída com `tkinter`.
- Inserção da URL do YouTube diretamente na tela.
- Seleção do diretório de destino usando o diálogo de diretórios do sistema.
- Exibição das qualidades e formatos disponíveis para o vídeo.
- Opção de fornecer um título personalizado para o arquivo de vídeo.
- Download do vídeo diretamente para o diretório escolhido.
- Caso nenhum título seja fornecido, o vídeo será salvo com o título original do YouTube.
## Stack utilizada

**Front-end:** Python - Tkinter

**Back-end:** Python - yt_dlp


## Como Executar o Projeto localmente

Clone o projeto

```bash
  git clone https://github.com/JO0OJ/YouTubeVideoDownloader
```

Entre no diretório do projeto

```bash
  cd nome-do-repositorio
```

Instale as dependências necessárias utilizando o `pip`

```bash
  pip install yt-dlp
```

Execute o script

```bash
  python nome_do_script.py
```

A interface gráfica será aberta. Insira a URL do vídeo do YouTube, selecione o diretório de destino e escolha a qualidade/formato desejado. Se necessário, forneça um título para o arquivo e clique no botão "Baixar Vídeo" para iniciar o download.


## Contribuindo

Contribuições são sempre bem-vindas!

- Faça um fork deste repositório.
- Crie uma branch para sua feature ou correção de bug (git checkout -b minha-feature).
- Faça as alterações desejadas e commit-as (git commit -am 'Adicionando nova feature').
- Faça o push para sua branch (git push origin minha-feature).
- Abra um pull request para revisão e inclusão no projeto.

Por favor, siga o `código de conduta` desse projeto.

