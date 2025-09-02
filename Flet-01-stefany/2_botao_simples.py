import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro Botão"
    page.padding = 20

    # Criando um texto que será modificado pelo botão
    mensagem = ft.Text(
        value="Clique no botão abaixo!",
        size=20,
        text_align=ft.TextAlign.CENTER,
    )

    def botao_clicado(evento):
        """
        Função chamada quando o botão é clicado.
        O parametro 'evento' contém informações sobre o evento de clique.
        """
        # Mudando o texto da mensagem
        mensagem.value = "Parabéns! Você clicou no botão."
        mensagem.color = ft.Colors.GREEN
        meu_botao.bgcolor = ft.Colors.LIGHT_GREEN_100
        meu_botao.color = ft.Colors.BLACK

        # IMPORTANTE: Sempre que modificamos elementos da interface,
        # precisamos chamar o método update() para que as mudanças apareçam na tela.
        page.update()
    
    # Criando um botão
    meu_botao = ft.ElevatedButton(
        text="Clique em mim!", # Texto que aparece no botão
        on_click=botao_clicado, # Função que será executada no clique
        width=200, # Largura do botão
        height=50, # Altura do botão
        bgcolor=ft.Colors.BLUE, # Cor de fundo do botão
        color=ft.Colors.WHITE, # Cor do texto do botão
    )

    #Adicionando os elementos na página
    page.add(mensagem)
    page.add(meu_botao)

ft.app(target=main)