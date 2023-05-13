from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador =p.chromium.launch(headless=False)
    pagina = navegador.new_pager()
    pagina.goto("https://seplan-layout-d.ikhon.com.br/proton/proton/login.aspx")
    time.sleep(5)