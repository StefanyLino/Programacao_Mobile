import flet as ft

def main(page: ft.Page):
    # Configurações da página principal
    page.title = "Calculadora de IMC" # título da janela
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # centraliza os elementos verticalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # centraliza os elementos horizontalmente

    # Campos de entrada de dados
    peso = ft.TextField(label="Peso (kg)", width=200, keyboard_type=ft.KeyboardType.NUMBER, border_color=ft.Colors.BROWN_300)
    altura = ft.TextField(label="Altura (m)", width=200, keyboard_type=ft.KeyboardType.NUMBER, color=ft.Colors.BROWN_300, border_color=ft.Colors.BROWN_300)

    # Texto onde o resultado será mostrado
    resultado = ft.Text(
        value="SEU RESULTADO APARECERÁ AQUI:",
        weight=ft.FontWeight.BOLD,
        size=15,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.BLACK
    )

    # Função para calcular o IMC
    def calcular_imc(e):
        try:
            # Converte os valores digitados em float (aceita vírgula e ponto)
            p: float = float(peso.value.replace(",", "."))
            a: float = float(altura.value.replace(",", "."))
            imc: float = p / (a ** 2)

            # Classificação do IMC com mensagens
            if imc < 18.5:
                resultado.value = f"Seu IMC é {imc:.2f}. Você está abaixo do peso."
                resultado.color = ft.Colors.BROWN_300
            elif 18.5 <= imc < 24.9:
                resultado.value = f"Seu IMC é {imc:.2f}. Você está com peso normal."
                resultado.color = ft.Colors.BROWN_300
            elif 25 <= imc < 29.9:
                resultado.value = f"Seu IMC é {imc:.2f}. Você está com sobrepeso."
                resultado.color = ft.Colors.BROWN_300
            else:
                resultado.value = f"Seu IMC é {imc:.2f}. Você está com obesidade."
                resultado.color = ft.Colors.BROWN_300

        # Caso o usuário digite valores inválidos
        except ValueError:
            resultado.value = "Por favor, insira valores válidos."
            resultado.color = ft.Colors.RED

        page.update() # atualiza a tela

    # Função para limpar os campos
    def limpar(e):
        peso.value = ""
        altura.value = ""
        resultado.value = "Seu resultado aparecerá aqui"
        resultado.color = ft.Colors.BLACK if page.bgcolor == ft.Colors.BROWN_300 else ft.Colors.BROWN_300
        page.update()

    # Função para alternar tema
    def alternar_tema(e):
        if page.bgcolor == ft.Colors.BROWN_200:
            page.bgcolor = ft.Colors.BLACK
            resultado.color = ft.Colors.BROWN_300
            tema_btn.label = "Tema Claro"
        else:
            page.bgcolor = ft.Colors.BROWN_200
            resultado.color = ft.Colors.BLACK
            tema_btn.label = "Tema Escuro"
        page.update()

    # Botão de alternar tema (um switch)
    tema_btn = ft.Switch(on_change=alternar_tema)

    # Adiciona todos os elementos na tela
    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "CALCULADORA DE IMC",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.BROWN_400   # 🔥 título marrom
                ),
                peso,
                altura,
                ft.Row(
                    controls=[
                        ft.ElevatedButton("CALCULAR", on_click=calcular_imc, bgcolor=ft.Colors.BROWN_300, color=ft.Colors.BLACK),
                        ft.ElevatedButton("LIMPAR", on_click=limpar, bgcolor=ft.Colors.BROWN_300, color=ft.Colors.BLACK)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
                resultado,
                ft.Row(
                    controls=[tema_btn],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

# Executa o app
ft.app(target=main)
