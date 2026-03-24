# Steam Discord Bot

Bot desenvolvido em Python utilizando **discord.py** que permite buscar jogos da Steam e exibir informações como preço, desconto e detalhes diretamente no Discord.

---

## Funcionalidades

*  Buscar jogos pelo nome
*  Listar múltiplos resultados
*  Exibir preço em Real (R$)
*  Mostrar desconto
*  Plataformas disponíveis
*  Data de lançamento
*  Link direto para a loja
*  Imagem do jogo
*  Comando de ajuda

---

##  Tecnologias utilizadas

* Python
* discord.py
* requests
* API pública da Steam

---

##  Instalação

1. Clone o projeto ou baixe os arquivos

2. Instale as dependências:


pip install -r requirements.txt


3. Configure seu token do Discord:

No final do arquivo `Steam Bot.py`, adicione:


bot.run("SEU_TOKEN_AQUI")


---

## ▶️ Como usar

### Buscar jogos pelo nome


!jogo resident evil


→ O bot retorna uma lista de jogos com ID



### Ver detalhes de um jogo


!preco 730


→ Exibe preço, desconto e informações completas

---

### Ver ajuda


!ajuda


---

##  Comandos disponíveis

| Comando        | Descrição                     |
| -------------- | ----------------------------- |
| !jogo <nome>   | Busca jogos pelo nome         |
| !preco <appid> | Mostra informações detalhadas |
| !ajuda         | Lista os comandos             |

---

## ⚠️ Configuração importante

Para o bot funcionar corretamente:

1. Acesse o Discord Developer Portal
2. Vá até a aba **Bot**
3. Ative a opção:

* ✅ Message Content Intent

---
