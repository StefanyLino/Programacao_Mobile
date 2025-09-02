import flet as ft

def main(page: ft.Page):
    page.title = "Campo de Texto"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

    # Campo de texto
    campo_nome = ft.TextField(
        label="Digite seu nome aqui",
        width=300,
        border_color=ft.Colors.BLUE
    )

    # Texto da resposta
    resposta = ft.Text(
        value="",
        size=18,
        text_align=ft.TextAlign.CENTER
    )

    # Imagem (começa "vazia")
    imagem = ft.Image(
        src="_",  # vazio = não aparece 
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )

    def processar_nome(evento):
        nome_digitado = campo_nome.value

        if nome_digitado == "" or nome_digitado is None:
            resposta.value = "Por favor, digite seu nome."
            resposta.color = ft.colors.RED
            imagem.src = ""  # não mostra imagem
        elif len(nome_digitado) < 2:
            resposta.value = "Nome muito curto!"
            resposta.color = ft.Colors.ORANGE
            imagem.src = ""  # não mostra imagem
        else:
            resposta.value = f"Olá, {nome_digitado}! Prazer em conhecê-lo."
            resposta.color = ft.Colors.GREEN
            # Mostra a imagem só se estiver tudo certo
            imagem.src = "https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif"

        page.update()

    # Botão
    botao_ok = ft.ElevatedButton(
        text="Confirmar",
        on_click=processar_nome,
        width=150,
    )

    # Adicionando na página
    page.add(
        ft.Text("Vamos nos conhecer!", size=22, weight=ft.FontWeight.BOLD),
        campo_nome,
        botao_ok,
        resposta,
        imagem,  # imagem já está na página, mas só aparece quando tiver src
    )

ft.app(target=main)
