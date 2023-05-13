from playwright.sync_api import sync_playwright
import time




with sync_playwright() as p:
    navegador =p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    #Tela de login SGD
    pagina.goto("https://seplan-layout-d.ikhon.com.br/proton/proton/login.aspx")
    pagina.locator('xpath=//*[@id="ctl00_cphSistema_txt_login"]').click()
  
    
    time.sleep(5)


