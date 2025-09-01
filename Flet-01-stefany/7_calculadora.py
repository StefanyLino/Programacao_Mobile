import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Simples"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

    # Campos e elementos
    numero1 = ft.TextField(label="Primeiro número", width=200, keyboard_type=ft.KeyboardType.NUMBER)
    numero2 = ft.TextField(label="Segundo número", width=200, keyboard_type=ft.KeyboardType.NUMBER)
    operacao = ft.Dropdown(
        label="Operação", width=200,
        options=[
            ft.dropdown.Option("Soma"), ft.dropdown.Option("Subtração"),
            ft.dropdown.Option("Multiplicação"), ft.dropdown.Option("Divisão")
        ]
    )
    resultado = ft.Text("Resultado aparecerá aqui", size=20, text_align=ft.TextAlign.CENTER, color=ft.Colors.GREY_600)

    def calcular(e):
        try:
            num1, num2, op = float(numero1.value), float(numero2.value), operacao.value

            if not op:
                resultado.value, resultado.color = "Selecione uma operação!", ft.Colors.ORANGE
            elif op == "Divisão" and num2 == 0:
                resultado.value, resultado.color = "Erro: Divisão por zero!", ft.Colors.RED
            else:
                simbolos = {"Soma": ("+", num1 + num2), "Subtração": ("-", num1 - num2),
                            "Multiplicação": ("×", num1 * num2), "Divisão": ("÷", num1 / num2)}
                simbolo, res = simbolos[op]
                resultado.value, resultado.color = f"{num1} {simbolo} {num2} = {res:.2f}", ft.Colors.GREEN
        except ValueError:
            resultado.value, resultado.color = "Digite números válidos!", ft.Colors.RED
        page.update()

    def limpar(e):
        numero1.value = numero2.value = operacao.value = ""
        resultado.value, resultado.color = "Campos limpos!", ft.Colors.BLUE
        page.update()

    # Interface
    page.add(
        ft.Column(
            [
                ft.Text("Calculadora Simples", size=24, weight=ft.FontWeight.BOLD),
                numero1, numero2, operacao,
                ft.Row(
                    [
                        ft.ElevatedButton("Calcular", on_click=calcular, width=150, bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
                        ft.ElevatedButton("Limpar", on_click=limpar, width=150, bgcolor=ft.Colors.GREY, color=ft.Colors.WHITE)
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                ft.Divider(),
                resultado
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
    )

ft.app(target=main)