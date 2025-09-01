import flet as ft

def main(page: ft.Page):
    # Configurações iniciais
    page.title = "Loja de Mangás"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.Colors.GREY_50

    # Estado do carrinho
    carrinho = []
    total_carrinho = 0.0

    # Área de produtos
    area_produtos = ft.GridView(
        expand=1,
        runs_count=2,
        max_extent=180,
        child_aspect_ratio=0.7,
        spacing=15,
        run_spacing=15
    )

    contador_carrinho = ft.Text("Carrinho (0)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    total_texto = ft.Text("Total: R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700)
    lista_carrinho = ft.ListView(height=150, spacing=5)
    notificacao = ft.Text(size=14, color=ft.Colors.BLUE_600, text_align=ft.TextAlign.CENTER)

    # Lista de mangás (use imagens locais ou URLs)
    mangas = [
        {"nome": "Naruto Vol. 1", "preco": 29.90, "categoria": "Shonen", "imagem": "naruto.jpg"},
        {"nome": "One Piece Vol. 1", "preco": 32.90, "categoria": "Shonen", "imagem": "onepiece.jpg"},
        {"nome": "Death Note Vol. 1", "preco": 35.00, "categoria": "Seinen", "imagem": "deathnote.jpg"},
        {"nome": "Attack on Titan Vol. 1", "preco": 34.90, "categoria": "Shonen", "imagem": "aot.jpg"},
        {"nome": "Dragon Ball Vol. 1", "preco": 31.90, "categoria": "Shonen", "imagem": "dragonball.jpg"},
        {"nome": "Tokyo Ghoul Vol. 1", "preco": 33.50, "categoria": "Seinen", "imagem": "tokyoghoul.jpg"},
    ]

    # Filtros
    filtro_categoria = ft.Dropdown(
        label="Categoria",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=150,
        value="Todas",
        color=ft.Colors.BLACK,
        options=[
            ft.dropdown.Option("Todas"),
            ft.dropdown.Option("Shonen"),
            ft.dropdown.Option("Seinen")
        ]
    )
    filtro_preco = ft.Dropdown(
        label="Preço",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        width=150,
        value="Todos",
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Até R$ 30"),
            ft.dropdown.Option("R$ 30-35"),
            ft.dropdown.Option("Acima R$ 35")
        ]
    )
    campo_busca = ft.TextField(
        label="Buscar mangá",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        width=200,
        prefix_icon=ft.Icons.SEARCH
    )

    # Funções
    def mostrar_notificacao(msg):
        notificacao.value = msg
        page.update()

    def atualizar_carrinho():
        contador_carrinho.value = f"Carrinho ({len(carrinho)})"
        total_texto.value = f"Total: R$ {total_carrinho:.2f}"
        lista_carrinho.controls.clear()
        for i, item in enumerate(carrinho):
            linha = ft.Row([
                ft.Text(item["nome"], expand=True),
                ft.Text(f"R$ {item['preco']:.2f}", color=ft.Colors.GREEN_600),
                ft.IconButton(
                    ft.Icons.DELETE,
                    icon_color=ft.Colors.RED,
                    on_click=lambda e, idx=i: remover_do_carrinho(idx)
                )
            ], spacing=10)
            lista_carrinho.controls.append(linha)
        page.update()

    def adicionar_ao_carrinho(nome, preco):
        nonlocal total_carrinho
        carrinho.append({"nome": nome, "preco": preco})
        total_carrinho += preco
        atualizar_carrinho()
        mostrar_notificacao(f"✅ {nome} adicionado!")

    def remover_do_carrinho(idx):
        nonlocal total_carrinho
        if 0 <= idx < len(carrinho):
            produto = carrinho.pop(idx)
            total_carrinho -= produto["preco"]
            atualizar_carrinho()
            mostrar_notificacao(f"❌ {produto['nome']} removido")

    def criar_card_manga(nome, preco, categoria, imagem):
        return ft.Container(
            content=ft.Column([
                ft.Image(src=imagem, width=100, height=140, fit=ft.ImageFit.CONTAIN),
                ft.Text(
                    nome,
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    max_lines=2,
                    overflow=ft.TextOverflow.ELLIPSIS
                ),
                ft.Text(
                    f"R$ {preco:.2f}",
                    size=12,
                    color=ft.Colors.GREEN_700,
                    text_align=ft.TextAlign.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5
            ),
            bgcolor=ft.Colors.WHITE,
            padding=10,
            border_radius=10,
            border=ft.border.all(1, ft.Colors.GREY_300),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK)
            ),
            on_click=lambda e, n=nome, p=preco: adicionar_ao_carrinho(n, p),
            ink=True
        )

    def carregar_mangas(e=None):
        area_produtos.controls.clear()
        categoria = filtro_categoria.value
        preco_faixa = filtro_preco.value
        busca = (campo_busca.value or "").lower()
        for manga in mangas:
            # Filtro categoria
            if categoria != "Todas" and manga["categoria"] != categoria:
                continue
            # Filtro preço
            if preco_faixa == "Até R$ 30" and manga["preco"] > 30:
                continue
            elif preco_faixa == "R$ 30-35" and not (30 < manga["preco"] <= 35):
                continue
            elif preco_faixa == "Acima R$ 35" and manga["preco"] <= 35:
                continue
            # Filtro busca
            if busca and busca not in manga["nome"].lower():
                continue
            card = criar_card_manga(
                manga["nome"], manga["preco"], manga["categoria"], manga["imagem"]
            )
            area_produtos.controls.append(card)
        page.update()

    def finalizar_compra(e):
        nonlocal total_carrinho
        if len(carrinho) > 0:
            carrinho.clear()
            total_carrinho = 0.0
            atualizar_carrinho()
            mostrar_notificacao("🎉 Compra finalizada! Obrigado!")
        else:
            mostrar_notificacao("⚠️ Carrinho vazio!")

    def limpar_filtros(e):
        filtro_categoria.value = "Todas"
        filtro_preco.value = "Todos"
        campo_busca.value = ""
        carregar_mangas()
        mostrar_notificacao("🧹 Filtros limpos!")
        page.update()

    # Eventos
    for controle in [filtro_categoria, filtro_preco, campo_busca]:
        controle.on_change = carregar_mangas

    # Carrega inicialmente
    carregar_mangas()

    # Layout
    page.add(
        ft.Column([
            ft.Text(
                "📚 Loja de Mangás",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_800,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Encontre os melhores mangás!",
                size=14,
                color=ft.Colors.GREY_600,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Row([filtro_categoria, filtro_preco], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            ft.Row([
                campo_busca,
                ft.ElevatedButton(
                    "🧹 Limpar Filtros",
                    on_click=limpar_filtros,
                    bgcolor=ft.Colors.ORANGE_400,
                    color=ft.Colors.WHITE,
                    height=40,
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)
                    )
                )
            ]),
            ft.Container(content=area_produtos, height=400, border=ft.border.all(1, ft.Colors.GREY_300), border_radius=10, padding=10),
            ft.Container(
                content=ft.Column([
                    ft.Row([contador_carrinho, total_texto], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    lista_carrinho,
                    ft.Row([
                        ft.ElevatedButton(
                            "🛒 Finalizar Compra",
                            on_click=finalizar_compra,
                            bgcolor=ft.Colors.GREEN,
                            color=ft.Colors.WHITE,
                            width=200
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    notificacao
                ], spacing=10),
                bgcolor=ft.Colors.WHITE,
                padding=20,
                border_radius=10,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=3,
                    color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)
                )
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
        )
    )

ft.app(target=main)
