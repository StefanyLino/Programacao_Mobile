# Flet com Python ⋆｡°✩
>Este repositório contém informações básicas sobre **Python** e **Flet**, além de um passo a passo para criar e executar um projeto simples com Flet.

---

## O que é Python

Python é uma **linguagem de programação de alto nível, interpretada, orientada a objetos e de código aberto**, conhecida por sua sintaxe clara e fácil de aprender. É amplamente utilizada em desenvolvimento web, ciência de dados, aprendizado de máquina, automação e em softwares para diversas áreas.

---

## O que é o Flet?

* **Flet não é uma linguagem** — é um *framework*.
* É relativamente recente e ainda está em desenvolvimento.
* Flet é um framework open-source que permite criar **aplicações web, desktop e mobile** utilizando **Python**, sem a necessidade de escrever HTML, CSS ou JavaScript.
* Características principais:

  * A aplicação roda em um servidor local ou na nuvem.
  * A interface pode ser exibida no navegador ou em um app Flet (desktop/mobile).
  * Comunicação entre o código Python e a interface é feita em **tempo real**.

---

## Requisitos

* Python instalado (versão compatível com Flet).
* Git (opcional, para controle de versão e criação do repositório).
* Acesso ao terminal / linha de comando.

---

## Passo a passo (rápido)

1. **Criar novo repositório** (local ou remoto).

2. **Criar e ativar um ambiente virtual** (exemplos):

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. **Instalar o Flet (desktop)**:

```bash
pip install flet-desktop
# (opcional) verificar a instalação / versão
pip show flet
```

4. **Executar o simulador / iniciar o app**:

```bash
# Executar em modo web (abre no navegador)
flet run --web nomeprojeto.py

```

> Observação: substitua `nomeprojeto.py` pelo nome do arquivo Python do seu projeto.

---

