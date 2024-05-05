import asyncio
from pyppeteer import launch

async def login_instagram(username, password):
    browser = await launch(
        headless=True,  # Executa sem interface gráfica
        args=[
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-infobars',
            '--window-position=0,0',
            '--ignore-certificate-errors',
            '--ignore-certificate-errors-spki-list',
            '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"',
            '--disable-blink-features=AutomationControlled'  # Desativa a flag de navegador automatizado
        ]
    )
    page = await browser.newPage()
    # Engana o JavaScript para pensar que não está rodando em modo headless
    await page.evaluateOnNewDocument('''() => {
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    }''')

    await page.goto('https://www.instagram.com/accounts/login/')

    # Espera pelo carregamento dos campos de entrada
    await page.waitForSelector('input[name="username"]')
    await page.type('input[name="username"]', username)
    await page.type('input[name="password"]', password)

    # Clica no botão de login usando um seletor CSS específico para o botão
    await page.waitForSelector('button[type="submit"]')
    await page.click('button[type="submit"]')

    # Espera para ser potencialmente redirecionado para a página inicial
    await page.waitForNavigation()
    print("Login realizado com sucesso!")
    await browser.close()

# Substitua 'your_username' e 'your_password' com suas credenciais reais
asyncio.run(login_instagram('seyzalel', 'Sey17zalel17@$'))
