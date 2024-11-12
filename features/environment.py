import os
from playwright.sync_api import sync_playwright
from config import config
from pages import login_page, invoice_details_page, invoice_list_page

def before_all(context):
    # Inicializa o Playwright e configura o navegador para headless ou não, com base na variável de ambiente
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)

def before_scenario(context, scenario):
    # Abre uma nova página no navegador para cada cenário de teste
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()
    context.page.set_default_timeout(config.TIMEOUT)
    context.login_page = login_page.LoginPage(context.browser_context)
    context.invoice_list_page = invoice_list_page.InvoiceListPage(context.browser_context)
    context.invoice_details_page = invoice_details_page.InvoiceDetailsPage(context.browser_context)

def after_scenario(context, scenario):
    # Fecha a página ao final de cada cenário
    context.page.close()

def after_all(context):
    # Fecha o navegador e encerra o Playwright após todos os testes
    context.browser.close()
    context.playwright.stop()
