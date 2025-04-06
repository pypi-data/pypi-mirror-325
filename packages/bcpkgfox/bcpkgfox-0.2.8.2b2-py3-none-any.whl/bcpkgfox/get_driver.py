from .find_elements import backcode__dont_use__find_element_with_wait_backcode, By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from typing import Optional

import undetected_chromedriver as uc

import logging
import random
import time
import sys
import os

logging.basicConfig(level=logging.ERROR)
class Webdriver:
    def __init__(self,
        version: Optional[str | int] = "latest",
        Selenoid: Optional[str] = None
        ):
        """Exempol Selenoid:
        Webdriver(Selenoid="remote_server_url='http://localhost:{SELF.PORTA}/wd/hub'")"""
        logging.basicConfig(
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[logging.StreamHandler(), logging.FileHandler(f'{self.__class__.__name__}.log')]
        )
        self.options = uc.ChromeOptions()
        self.version_main = version

        self.captcha_api_key = None
        self.extension_path = None
        self.captcha_name = None
        self.driver = None

        self.arguments = Arguments(self)

    def initialize_driver(self,
        subprocess: Optional[bool] = True,
        maximize: Optional[bool] = True
        ):
        self.driver = uc.Chrome(options=self.options, remote_server_url=Selenoid, version_main=self.version_main, use_subprocess=subprocess)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        if maximize: self.maximize_window()
        return self.driver

    def add_extension(self, extension_folder: str,
        config: Optional[bool] = False,
        key: Optional[str|int] = None
        ):
        """ Inicia o navegador com uma extensão, o 'config' ele identifica o nome da pasta e se for uma conhecida (capmonster, twocaptcha) configura automaticamente
        - OBS: Caso a extensão precise de alguma KEY, declare ela também na variavel "key"
        - Exemplo: add_extension("capmonster", config=True)"""
        try:
            extensao_caminho = self.__resource_path(extension_folder)
            if not os.path.exists(extensao_caminho): extensao_caminho = os.path.abspath(extension_folder)
            self.arguments.add_new_argument(f'--load-extension={extensao_caminho}')
        except Exception as e:
            logging.error("Erro ao verificar pasta da extensão", exc_info=True)
            raise SystemError("Verificar pasta da extensão") from e

        if key:
            key = str(key) ; cap_monster_names = ["capmonster", "captchamonster", "monster", "cap-monster", "captcha monster", "captcha-monster", "cmonster", "cap monster"]
            for name in cap_monster_names:
                if name in extension_folder.lower(): self._config_capmonster(key)

    class Arguments:
        def __init__(self, self_bot):
            self.Webdriver = self_bot
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                handlers=[logging.StreamHandler(), logging.FileHandler(f'{self.__class__.__name__}.log')]
            )

        def add_new_argument(self, Args: str | list):
            """ Coloque apenas o argumento que você quer adicionar a inicialização do driver.
            - Exemplo singular: add_new_argument("--headless")
            - Exemplo composto: add_new_argument(["--headless", "--disable-gpu", ... ])"""

            if isinstance(args,list) == True:
                for arg in args: self.Webdriver.options.add_argument(arg)
            else: self.Webdriver.options.add_argument(args)

        def add_experimental_new_option(self, Args: str | list):
            """ Coloque apenas o argumento que você quer adicionar a inicialização do driver.
            - Exemplo: add_experimental_new_option("prefs", profile)"""

            if isinstance(args,list) == True:
                for arg in args: self.Webdriver.options.add_experimental_option [arg]
            else: self.Webdriver.options.add_experimental_option[args]

    def _config_capmonster(self, api_key: str) -> None:
        self.driver.get("chrome://extensions/") ; time.sleep(5)

        # Shadow-doom
        id_extension = self.driver.execute_script("""
            return document.querySelector('extensions-manager')
            .shadowRoot.querySelector('extensions-item-list')
            .shadowRoot.querySelector('extensions-item').id;
        """) ; print("ID extensão extraido:", id_extension)

        self.driver.get(f"chrome-extension://{id_extension.lower()}/popup.html")

        backcode__dont_use__find_element_with_wait_backcode(self.driver, By.ID, "client-key-input").send_keys(api_key) ; time.sleep(2.5)
        backcode__dont_use__find_element_with_wait_backcode(self.driver, By.XPATH, '//label[span[input[@id="captcha-radio-token-ReCaptcha2"]]]').click()
        backcode__dont_use__find_element_with_wait_backcode(self.driver, By.ID, "client-key-save-btn").click()
        print(" - Capmonter configurado.")

    @staticmethod
    def __resource_path(relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def backcode__dont_use__set_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    ]
    return random.choice(user_agents)

def backcode__dont_use__launch_browser(download_dir: str, extension_path, captcha_name, captcha_api_key) -> WebElement:
    global driver

    # Configurações para o Chrome
    options = uc.ChromeOptions()

    # Alterar o User-Agent
    options.add_argument(f"user-agent={backcode__dont_use__set_user_agent()}")

    # Default's
    profile = {
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'download.default_directory': download_dir,
    }
    options.add_experimental_option('prefs', profile)

    # Configurações para reduzir detecção
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-infobars')

    if extension_path:
        extensao_caminho = resource_path(extension_path)
        if not os.path.exists(extensao_caminho):
            extensao_caminho = os.path.abspath(extension_path)

        options.add_argument(f'--load-extension={extensao_caminho}')

    # options.add_argument('--disable-extensions') # Fix: Possibilita ter extensões ou não, nunca influenciou na detecção

    # Inicializar o navegador com undetected_chromedriver
    driver = uc.Chrome(options=options, use_subprocess=True)

    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    if captcha_name:
        cap_monster_names = ["capmonster", "captchamonster", "monster", "cap-monster", "captcha monster", "captcha-monster", "cmonster", "cap monster"]

        for name in cap_monster_names:
            if captcha_name.lower() == name:
                backcode__dont_use__capmonster(captcha_api_key)

    driver.maximize_window()
    return driver

def backcode__dont_use__get(driver, link) -> WebElement:
    driver.get(link)

def backcode__dont_use__capmonster(api_key) -> None:
    global driver

    driver.get("chrome://extensions/")
    time.sleep(5)

    # Pega por JS pois está dentro da shadow
    id_extension = driver.execute_script("""
        return document.querySelector('extensions-manager')
        .shadowRoot.querySelector('extensions-item-list')
        .shadowRoot.querySelector('extensions-item').id;
    """)

    print("ID extensão extraido:", id_extension)
    driver.get(f"chrome-extension://{id_extension.lower()}/popup.html")

    backcode__dont_use__find_element_with_wait_backcode(driver, By.ID, "client-key-input").send_keys(api_key)
    time.sleep(2.5)
    backcode__dont_use__find_element_with_wait_backcode(driver, By.XPATH, '//label[span[input[@id="captcha-radio-token-ReCaptcha2"]]]').click() # icone salvar
    backcode__dont_use__find_element_with_wait_backcode(driver, By.ID, "client-key-save-btn").click() # icone salvar
    print(" - Capmonter configurado.")