# Importa a biblioteca Flet para criar interfaces gráficas
import flet as ft

def criar_card_inseto(nome, emoji, descricao, cor):
    """
    Função que cria um card (cartão) visual para cada inseto.
    """
    return ft.Container(
        content=ft.Column([
            ft.Text(emoji, size=40, text_align=ft.TextAlign.CENTER),
            ft.Text(nome, size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ft.Text(descricao, size=12, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER)
        ], 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=8
        ),
        bgcolor=cor,
        padding=20,
        border_radius=15,
        width=160,
        height=140,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=8,
            color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK)
        )
    )

def main(page: ft.Page):
    page.title = "Insectário Virtual"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO

    # Lista com diferentes insetos
    insetos = [
        {"nome": "Borboleta", "emoji": "🦋", "descricao": "Colorida e delicada", 
         "cor": ft.Colors.PINK_400, "categoria": "Voador", "tamanho": "Médio"},
        {"nome": "Abelha", "emoji": "🐝", "descricao": "Produz mel e poliniza flores", 
         "cor": ft.Colors.AMBER_400, "categoria": "Voador", "tamanho": "Pequeno"},
        {"nome": "Joaninha", "emoji": "🐞", "descricao": "Pequena protetora das plantas", 
         "cor": ft.Colors.RED_400, "categoria": "Terrestre", "tamanho": "Pequeno"},
        {"nome": "Formiga", "emoji": "🐜", "descricao": "Organizada e trabalhadora", 
         "cor": ft.Colors.BROWN_400, "categoria": "Terrestre", "tamanho": "Pequeno"},
        {"nome": "Besouro", "emoji": "🪲", "descricao": "Diversidade impressionante", 
         "cor": ft.Colors.GREEN_600, "categoria": "Terrestre", "tamanho": "Médio"},
        {"nome": "Grilo", "emoji": "🦗", "descricao": "Canta nas noites quentes", 
         "cor": ft.Colors.LIME_500, "categoria": "Terrestre", "tamanho": "Médio"},
        {"nome": "Tarântula", "emoji": "🕷️", "descricao": "Assustadora, mas inofensiva", 
         "cor": ft.Colors.CYAN_400, "categoria": "Voador", "tamanho": "Médio"},
        {"nome": "Mosquito", "emoji": "🦟", "descricao": "Pequeno, mas insistente", 
         "cor": ft.Colors.GREY_500, "categoria": "Voador", "tamanho": "Pequeno"}
    ]

    area_cards = ft.GridView(
        expand=1,
        runs_count=2,
        max_extent=180,
        child_aspect_ratio=1.0,
        spacing=15,
        run_spacing=15
    )

    filtro_categoria = ft.Dropdown(
        label="Categoria",
        width=150,
        value="Todos",
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Voador"),
            ft.dropdown.Option("Terrestre"),
            ft.dropdown.Option("Saltador")
        ]
    )

    filtro_tamanho = ft.Dropdown(
        label="Tamanho",
        width=150,
        value="Todos",
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Pequeno"),
            ft.dropdown.Option("Médio"),
            ft.dropdown.Option("Grande")
        ]
    )

    campo_busca = ft.TextField(
        label="Buscar",
        width=150,
        prefix_icon=ft.Icons.SEARCH
    )

    contador = ft.Text("", size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER)

    def carregar_cards(e=None):
        area_cards.controls.clear()
        categoria = filtro_categoria.value
        tamanho = filtro_tamanho.value
        busca = (campo_busca.value or "").lower()

        filtrados = [i for i in insetos
                     if (categoria == "Todos" or i["categoria"] == categoria) and
                        (tamanho == "Todos" or i["tamanho"] == tamanho) and
                        (not busca or busca in i["nome"].lower())]

        for inseto in filtrados:
            card_do_inseto = criar_card_inseto(
                inseto["nome"], inseto["emoji"], inseto["descricao"], inseto["cor"]
            )
            area_cards.controls.append(card_do_inseto)

        total_filtrados = len(filtrados)
        total_geral = len(insetos)

        if total_filtrados == total_geral:
            contador.value = f"Mostrando todos os {total_filtrados} insetos"
        else:
            contador.value = f"Encontrados {total_filtrados} de {total_geral} insetos"

        page.update()

    def limpar_filtros(e):
        filtro_categoria.value = "Todos"
        filtro_tamanho.value = "Todos"
        campo_busca.value = ""
        carregar_cards()

    for controle in [filtro_categoria, filtro_tamanho, campo_busca]:
        controle.on_change = carregar_cards

    carregar_cards()

    page.add(
        ft.Column([
            ft.Text("🪲 Insectário Virtual", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Text("Explore diferentes tipos de insetos", size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
            ft.Row([filtro_categoria, filtro_tamanho], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            ft.Row([
                campo_busca,
                ft.ElevatedButton("🧹 Limpar", on_click=limpar_filtros, bgcolor=ft.Colors.GREY_400, color=ft.Colors.WHITE)
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            contador,
            ft.Container(
                content=area_cards,
                height=400,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=10,
                padding=10
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15)
    )

ft.app(target=main)
