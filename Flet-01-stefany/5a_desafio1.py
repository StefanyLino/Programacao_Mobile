import flet as ft

def main(page: ft.Page):
    page.title = "Criador de Perfil"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO

    # Estado
    foto_usuario = {"path": None}

    # --- Campos ---
    campo_nome = ft.TextField(label="Nome completo", width=300, on_change=lambda e: atualizar_preview())
    campo_idade = ft.TextField(label="Idade", width=300, keyboard_type=ft.KeyboardType.NUMBER,
                               on_change=lambda e: atualizar_preview())
    dropdown_hobby = ft.Dropdown(
        label="Hobby favorito",
        width=300,
        options=[
            ft.dropdown.Option("Leitura 📚"),
            ft.dropdown.Option("Esportes ⚽"),
            ft.dropdown.Option("Música 🎵"),
            ft.dropdown.Option("Jogos 🎮"),
            ft.dropdown.Option("Culinária 🍳"),
            ft.dropdown.Option("Arte 🎨"),
            ft.dropdown.Option("Viagens ✈️"),
            ft.dropdown.Option("Tecnologia 💻"),
        ],
        on_change=lambda e: atualizar_preview()
    )

    # --- Cartão de pré-visualização (invisível no início) ---
    cartao_preview = ft.Container(
        bgcolor=ft.Colors.WHITE,
        padding=30,
        border_radius=15,
        width=350,
        visible=False  # <- invisível inicialmente
    )

    # --- Área de aviso de erro ---
    aviso = ft.Container(visible=False)

    # --- FilePicker ---
    def on_file_picked(e: ft.FilePickerResultEvent):
        if e.files:
            arq = e.files[0]
            nome = arq.name.lower()
            if not (nome.endswith(".jpg") or nome.endswith(".jpeg") or nome.endswith(".png")):
                mostrar_erro("Apenas imagens JPG ou PNG são permitidas")
                return
            foto_usuario["path"] = arq.path
            botao_foto.text = "Imagem escolhida ✅"
            atualizar_preview()

    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    botao_foto = ft.ElevatedButton(
        "Escolher Foto",
        icon=ft.Icons.PHOTO,
        on_click=lambda _: file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["jpg", "jpeg", "png"]
        )
    )

    # --- Funções auxiliares ---
    def categoria_e_cor():
        try:
            i = int(campo_idade.value)
        except Exception:
            return None, ft.Colors.PURPLE
        if i < 18:
            return "Jovem", ft.Colors.GREEN
        if i < 60:
            return "Adulto", ft.Colors.BLUE
        return "Experiente", ft.Colors.PURPLE

    def atualizar_preview(final=False):
        categoria, cor = categoria_e_cor()

        if foto_usuario["path"]:
            avatar = ft.Image(
                src=foto_usuario["path"],
                width=72, height=72,
                fit=ft.ImageFit.COVER,
                border_radius=ft.border_radius.all(36),
            )
        else:
            avatar = ft.Icon(ft.Icons.PERSON, size=72, color=cor)

        nome_txt = campo_nome.value.strip() if campo_nome.value else "Seu nome"
        if campo_idade.value and categoria:
            idade_txt = f"{campo_idade.value} anos - {categoria}"
        else:
            idade_txt = "Idade - Categoria"

        hobby_txt = f"Hobby: {dropdown_hobby.value}" if dropdown_hobby.value else "Hobby: —"

        cartao_preview.content = ft.Column(
            [
                avatar,
                ft.Text(nome_txt, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_400),
                ft.Text(idade_txt, size=14, color=ft.Colors.GREY_600),
                ft.Text(hobby_txt, size=14, color=ft.Colors.GREY_400),
                ft.Container(
                    content=ft.Text("Pré-visualização ✨" if not final else "Perfil Criado 🎉", color=ft.Colors.WHITE),
                    bgcolor=cor,
                    padding=10,
                    border_radius=20
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
        page.update()

    def mostrar_erro(msg: str):
        aviso.content = ft.Column(
            [
                ft.Icon(ft.Icons.ERROR, color=ft.Colors.RED, size=40),
                ft.Text(msg, color=ft.Colors.RED, text_align=ft.TextAlign.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
        aviso.bgcolor = ft.Colors.RED_50
        aviso.padding = 20
        aviso.border_radius = 15
        aviso.visible = True
        page.update()

    def criar_perfil(e):
        if not campo_nome.value or len(campo_nome.value.strip()) < 2:
            mostrar_erro("Nome deve ter pelo menos 2 caracteres")
            return
        if not campo_idade.value:
            mostrar_erro("Idade é obrigatória")
            return
        try:
            i = int(campo_idade.value)
            if i < 1 or i > 120:
                mostrar_erro("Idade deve estar entre 1 e 120 anos")
                return
        except ValueError:
            mostrar_erro("Idade deve ser um número")
            return
        if not dropdown_hobby.value:
            mostrar_erro("Selecione um hobby")
            return
        if not foto_usuario["path"]:
            mostrar_erro("Selecione uma foto")
            return

        # Se tudo ok, mostra o cartão final
        atualizar_preview(final=True)
        cartao_preview.visible = True
        aviso.visible = False
        page.snack_bar = ft.SnackBar(ft.Text("Perfil validado! ✅"))
        page.snack_bar.open = True
        page.update()

    def limpar(e):
        campo_nome.value = ""
        campo_idade.value = ""
        dropdown_hobby.value = None
        foto_usuario["path"] = None
        botao_foto.text = "Escolher Foto"
        aviso.visible = False
        cartao_preview.visible = False
        atualizar_preview()
        page.update()

    # --- Botões principais ---
    linha_botoes = ft.Row(
        [
            ft.ElevatedButton("Criar Perfil", on_click=criar_perfil, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE, width=140),
            ft.ElevatedButton("Limpar", on_click=limpar, bgcolor=ft.Colors.GREY, color=ft.Colors.WHITE, width=140),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # --- Layout ---
    layout = ft.Column(
        [
            ft.Text("Criador de Perfil", size=26, weight=ft.FontWeight.BOLD),
            ft.Container(height=20),
            campo_nome,
            campo_idade,
            dropdown_hobby,
            botao_foto,
            ft.Container(height=10),
            cartao_preview,   # cartão reservado, mas invisível até criar perfil
            ft.Container(height=10),
            linha_botoes,
            ft.Container(height=10),
            aviso,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    page.add(layout)
    atualizar_preview()  # monta a prévia inicial (apenas ícone)

ft.app(target=main)
