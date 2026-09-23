# Tradutor de Fala

Programa em Python que **ouve o que você fala e traduz em tempo real**, mostrando (ou falando) a tradução automaticamente.

## O que ele faz

- Escuta o microfone e transforma a fala em texto
- Traduz esse texto para o idioma escolhido
- Mostra a tradução na tela e/ou fala ela em voz alta

Útil pra conversar com alguém que fala outro idioma, ou pra treinar pronúncia e tradução na hora.

## Tecnologias usadas

Python

## Como instalar

1. Baixe o projeto:
```bash
git clone https://github.com/beneditodossantosjoao027-cloud/tradutor-de-fala.git
cd tradutor-de-fala
```

2. Instale o Python (versão 3.10 ou mais nova) no site oficial: https://www.python.org/downloads/ — durante a instalação, marque a opção "Add Python to PATH".

3. Instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

## Como usar

1. Conecte um microfone ao computador (a maioria dos notebooks já tem um embutido).
2. Rode o programa:
```bash
python tradutor_de_fala.py
```
3. Fale normalmente perto do microfone.
4. A tradução aparece na tela (e/ou é falada, dependendo da configuração do programa).
5. Para fechar, feche a janela ou aperte a tecla ESC.

## Segurança

O programa só usa o microfone enquanto está aberto e rodando — ele não grava nem guarda áudio no seu computador, apenas envia o texto reconhecido para o serviço de tradução e descarta em seguida. Nenhum dado pessoal é coletado.

## Autor

Benedito dos Santos — [GitHub](https://github.com/beneditodossantosjoao027-cloud)
