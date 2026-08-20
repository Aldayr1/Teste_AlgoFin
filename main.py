from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen




# Colocamos o design diretamente no arquivo principal para o primeiro teste
KV = '''
MDScreenManager:
    InicialScreen:
    SobreScreen:

<InicialScreen>:
    name: 'inicial'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "AlgoFin - Início"
            md_bg_color: app.theme_cls.primary_color
        MDLabel:
            text: "Sucesso! O App abriu no Android!"
            halign: "center"
            font_style: "H5"
        MDRaisedButton:
            text: "Ir para Sobre"
            pos_hint: {"center_x": .5}
            on_release: app.root.current = 'sobre'
        Widget: 

<SobreScreen>:
    name: 'sobre'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "AlgoFin - Sobre"
            md_bg_color: app.theme_cls.primary_color
        MDLabel:
            text: "Educação Financeira e Computação"
            halign: "center"
        MDRaisedButton:
            text: "Voltar"
            pos_hint: {"center_x": .5}
            on_release: app.root.current = 'inicial'
        Widget:
'''

# Telas simplificadas
class InicialScreen(MDScreen):
    pass

class SobreScreen(MDScreen):
    pass

# Aplicativo Principal
class AlgoFinApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        # Carrega o layout simplificado
        return Builder.load_string(KV)

if __name__ == '__main__':
    AlgoFinApp().run()
