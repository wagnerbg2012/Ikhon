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
        
        if not self.find( "senha", matching=0.97, waiting_time=10000):
            self.not_found("senha")
        self.click()
        self.paste("1234")
        
        if not self.find( "entrar", matching=0.97, waiting_time=10000):
            self.not_found("entrar")
        self.click()
        
        
        if not self.find( "documentos", matching=0.97, waiting_time=10000):
            self.not_found("documentos")
        self.click()
        
        if not self.find( "incluir", matching=0.97, waiting_time=10000):
            self.not_found("incluir")
        self.click()
        
        
        if not self.find( "assunto", matching=0.97, waiting_time=10000):
            self.not_found("assunto")
        self.click()
        self.paste("dsafsadsadsdfdsfsd")
        
        if not self.find( "especie", matching=0.97, waiting_time=10000):
            self.not_found("especie")
        self.click()
        
        if not self.find( "alvara", matching=0.97, waiting_time=10000):
            self.not_found("alvara")
        self.click()
        
        if not self.find( "classificacao", matching=0.97, waiting_time=10000):
            self.not_found("classificacao")
        self.click()
        
        if not self.find( "relatorio", matching=0.97, waiting_time=10000):
            self.not_found("relatorio")
        self.click()
        
        if not self.find( "interessados", matching=0.97, waiting_time=10000):
            self.not_found("interessados")
        self.click()
        
        if not self.find( "nome", matching=0.97, waiting_time=10000):
            self.not_found("nome")
        self.click()
        self.paste("wedson silva")
        
        if not self.find( "pesquisar", matching=0.97, waiting_time=10000):
            self.not_found("pesquisar")
        self.click()
        
        if not self.find( "selecionar", matching=0.97, waiting_time=10000):
            self.not_found("selecionar")
        self.click()
        
        if not self.find( "incluir usuario", matching=0.97, waiting_time=10000):
            self.not_found("incluir usuario")
        self.click()
        
        

       
        
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

