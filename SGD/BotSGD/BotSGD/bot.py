"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
import time
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        self.browse("https://seplan-layout-d.ikhon.com.br/")
        if not self.find( "CPF", matching=0.97, waiting_time=10000):
            self.not_found("CPF")
        self.click()
        self.paste("023.020.731-69")
        time.sleep(1)
        # Wfs- tela inicial- informar CPF_17/05/2023
        if not self.find( "senha", matching=0.97, waiting_time=10000):
            self.not_found("senha")
        self.click()
        self.paste("1234")
        time.sleep(1)
        # Wfs- tela inicial- informar senha_17/05/2023
        if not self.find( "entrar", matching=0.97, waiting_time=10000):
            self.not_found("entrar")
        self.click()
        time.sleep(1)        
        # Wfs- tela inicial- entrar no sistema _17/05/2023
        if not self.find( "documentos", matching=0.97, waiting_time=10000):
            self.not_found("documentos")
        self.click()
        time.sleep(1)
        # Wfs- clicar no campo "Documentos" _17/05/2023
        if not self.find( "incluir", matching=0.97, waiting_time=10000):
            self.not_found("incluir")
        self.click()
        time.sleep(1)        
        # Wfs- clicar no campo"incluir"_17/05/2023
        if not self.find( "assunto", matching=0.97, waiting_time=10000):
            self.not_found("assunto")
        self.click()
        self.paste("dsafsadsadsdfdsfsd")
        time.sleep(1)
        # Wfs- informar o assunto na descrição do campo_17/05/2023
        if not self.find( "especie", matching=0.97, waiting_time=10000):
            self.not_found("especie")
        self.click()
        time.sleep(1)
        # Wfs- selecionar a caixa de espécie documental_17/05/2023
        if not self.find( "alvara", matching=0.97, waiting_time=10000):
            self.not_found("alvara")
        self.click()
        time.sleep(1)
        # Wfs- selecionar o tipo de espécie documental_17/05/2023
        if not self.find( "classificacao", matching=0.97, waiting_time=10000):
            self.not_found("classificacao")
        self.click()
        time.sleep(1)
        # Wfs- selecionar o campo de classificação arquivistica_17/05/2023
        if not self.find( "relatorio", matching=0.97, waiting_time=10000):
            self.not_found("relatorio")
        self.click()
        time.sleep(1)
        # Wfs- selecionar o tipo de classificação arquivistica_17/05/2023
        if not self.find( "interessados", matching=0.97, waiting_time=10000):
            self.not_found("interessados")
        self.click()
        time.sleep(1)
        # Wfs- selecionar o campo de interessados_17/05/2023
        if not self.find( "nome", matching=0.97, waiting_time=10000):
            self.not_found("nome")
        self.click()
        time.sleep(1)
        self.paste("wedson silva")
        time.sleep(1)
        # Wfs- clicar no campo e escrever o nome do interessado_17/05/2023
        if not self.find( "pesquisar", matching=0.97, waiting_time=10000):
            self.not_found("pesquisar")
        self.click()
        time.sleep(1)
        # Wfs- clicar no botão de pesquisa_17/05/2023
        if not self.find( "selecionar", matching=0.97, waiting_time=10000):
            self.not_found("selecionar")
        self.click()
        time.sleep(1)
        # Wfs- Selecionar o nome digitado no campo de pesquisa_17/05/2023
        if not self.find( "incluir usuario", matching=0.97, waiting_time=10000):
            self.not_found("incluir usuario")
        self.click()
        time.sleep(1)
        # Wfs- incluir o usuário_17/05/2023
        if not self.find( "escolher arquivo", matching=0.97, waiting_time=10000):
            self.not_found("escolher arquivo")
        self.click()
        time.sleep(1)
        # Wfs- clicar no botão arquivo digital_17/05/2023
        if not self.find( "selecionar arquivo", matching=0.97, waiting_time=10000):
            self.not_found("selecionar arquivo")
        self.click()
        time.sleep(1)
        # Wfs- Selecionar o tipo de arquivo digital_17/05/2023
        if not self.find( "abrir arquivo", matching=0.97, waiting_time=10000):
            self.not_found("abrir arquivo")
        self.click()
        time.sleep(1)
        # Wfs- escolher o arquivo degital dentro de documentos_17/05/2023
        if not self.find( "adicionar arquivo", matching=0.97, waiting_time=10000):
            self.not_found("adicionar arquivo")
        self.click()
        time.sleep(1)
        # Wfs- Selecionar o arquivo digital_17/05/2023
        if not self.find( "carregar pagina", matching=0.97, waiting_time=10000):
            self.not_found("carregar pagina")                  
        self.scroll_down(1000)
        time.sleep(1)
        # Wfs- Função adicionada para carregar a pagina e rolar para baixo_17/05/2023

        if not self.find( "incluir o documento", matching=0.97, waiting_time=10000):
            self.not_found("incluir o documento")
        self.click()
        #Incluir o documento no sistema.
        
        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()

