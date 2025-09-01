import flet as ft

def main(page: ft.Page):
    txt_name = ft.TextField(label="Seu nome")
    def btn_click(e):
        page.add(ft.Text(f"Olá, {txt_name.value}!"))
    page.add(txt_name, ft.ElevatedButton("Dizer Olá", on_click=btn_click))

ft.app(target=main)

