import flet as ft

def main(page: ft.Page):
    page.title = "Seletor de Cores"
    page.padding = 20

    # Container que mudará de cor (como uma caixa colorida)
    caixa_colorida = ft.Container(
        content=ft.Text(
            "Escolha uma cor!",
            color=ft.Colors.WHITE,
            size=18,
            text_align=ft.TextAlign.CENTER,
        ),
        bgcolor=ft.Colors.GREY,
        width=300,
        height=100,
        border_radius=10,
        alignment=ft.alignment.center, 
    )

    def cor_selecionada(evento):
        """
        Função é executada sempre que o usuário escolhe uma cor.
        """

        # Pegando qual cor foi escolhida
        cor_escolhida = evento.control.value

        # Dicionário com as cores disponíveis
        # É como uma "lista de correspondência" entre nome e cor real
        cores_disponiveis = {
            "Vermelho": ft.Colors.RED,
            "Verde": ft.Colors.GREEN,
            "Azul": ft.Colors.BLUE,
            "Amarelo": ft.Colors.YELLOW,
            "Roxo": ft.Colors.PURPLE,
            "Laranja": ft.Colors.ORANGE,
            "Rosa": ft.Colors.PINK
        }

        # Mudando a cor da caixa
        caixa_colorida.bgcolor = cores_disponiveis[cor_escolhida]
        caixa_colorida.content.value = f"Cor selecionada: {cor_escolhida}"

        page.update()
    
    # Criando o Dropdown (lista suspensa)
    seletor_cor = ft.Dropdown(
        label="Escolha uma cor",
        width=200,
        options=[
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Roxo"),
            ft.dropdown.Option("Laranja"),
            ft.dropdown.Option("Rosa")
        ],
        on_change=cor_selecionada
    )

    # Adicionando os componentes na página
    page.add(
        ft.Text("Seletor de Cores Mágico!", size=24, weight=ft.FontWeight.BOLD),
        seletor_cor,
        caixa_colorida
    )

ft.app(target=main)