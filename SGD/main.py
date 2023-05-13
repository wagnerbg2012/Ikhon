from playwright.sync_api import sync_playwright
import time
import subprocess



with sync_playwright() as p:
    navegador =p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://seplan-layout-d.ikhon.com.br/proton/proton/login.aspx")
    subprocess.call(["python", "Faz_login.py"])
    time.sleep(5)


