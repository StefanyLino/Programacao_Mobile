import flet as ft

def main(page: ft.Page):
    """
    Função principal que será executada quando o app iniciar.
    O parâmetro 'page' representa a página do aplicativo.
    """

    # Configurações básicas da página
    page.title = "Meu Primeiro App Flet" # Título da aba
    page.padding = 20 # Espaçamento interno da página

    # Criando nosso primeiro elemento: um texto
    meu_texto = ft.Text(
        value="Hello world! (Primeiro app com Flet!)", # Conteúdo do texto
        size=24, # Tamanho da fonte
        color=ft.Colors.BLUE, # Cor do texto
        weight=ft.FontWeight.BOLD, # Peso da fonte (negrito)
        text_align=ft.TextAlign.CENTER # Alinhamento do texto
    )

    # Adicionando o texto à página
    page.add(meu_texto)

    # Vamos adicionar mais alguns elementos para deixar a página mais interessante
    page.add(
        ft.Text("Bem-vindo ao mundo do desenvolvimento mobile", size=16),
        ft.Text("Com Flet, você pode criar apps incríveis", size=16, color=ft.Colors.GREEN)
    )

# Esta linha inicia nosso aplicativo, chamando a função main
ft.app(target=main)
