from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:

    # Seção De e Para
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Fluxo de chamada de táxi
    taxi_option = (
        By.XPATH,
        '//button[contains(text(),"Chamar")]'
    )

    # Plano Comfort
    comfort_icon = (
        By.XPATH,
        '//img[contains(@src,"kids")]'
    )

    # Plano Comfort selecionado
    comfort_active = (
        By.XPATH,
        '//img[contains(@src,"kids")]'
        '/ancestor::*[contains(@class,"active")]'
    )

    # Telefone
    phone_field = (By.ID, 'phone')
    phone_next_button = (
        By.XPATH,
        '//button[contains(text(), "Avançar")]'
    )
    phone_code_field = (By.ID, 'code')

    # Cartão
    payment_method = (
        By.XPATH,
        '//div[contains(@class, "pp-value")]'
    )

    add_card_button = (
        By.XPATH,
        '//button[contains(text(), "Adicionar cartão")]'
    )

    card_number_field = (By.ID, 'number')

    card_code_field = (By.ID, 'code')

    card_add_button = (
        By.XPATH,
        '//button[contains(text(), "Adicionar")]'
    )

    # Comentário para o motorista
    comment_field = (By.ID, 'comment')

    # Cobertor
    blanket_switch = (
        By.XPATH,
        '//div[contains(@class, "r-switch")]'
        '[.//span[contains(text(), "Cobertor")]]'
    )

    # Estado do cobertor
    blanket_checked = (
        By.XPATH,
        '//div[contains(@class, "r-switch")]'
        '[.//span[contains(text(), "Cobertor")]]'
        '//input[@type="checkbox"]'
    )

    # Sorvete
    ice_cream_plus = (
        By.XPATH,
        '//div[contains(@class, "counter")]'
        '[.//span[contains(text(), "Sorvete")]]'
        '//button[contains(@class, "counter-plus")]'
    )

    # Modal de busca de carros
    car_search_modal = (
        By.XPATH,
        '//div[contains(@class, "modal")]'
        '[contains(@class, "search")]'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Métodos auxiliares

    def _find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def _click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator):
        return self._find(locator).text

    def _get_value(self, locator):
        return self._find(locator).get_attribute("value")

    # Endereço

    def enter_locations(self, from_text, to_text):
        self._type(self.from_field, from_text)
        self._type(self.to_field, to_text)

    def get_from_location(self):
        return self._get_value(self.from_field)

    def get_to_location(self):
        return self._get_value(self.to_field)

    # Chamar Táxi

    def click_taxi_option(self):
        self._click(self.taxi_option)

    # Comfort

    def click_comfort_icon(self):
        self._click(self.comfort_icon)

    def click_comfort_active(self):
        active_button = self.wait.until(
            EC.visibility_of_element_located(
                self.comfort_active
            )
        )

        print(
            "ELEMENTO ENCONTRADO:",
            active_button
        )

        print(
            "CLASSE:",
            active_button.get_attribute("class")
        )

        return "active" in active_button.get_attribute("class")

    # Telefone

    def enter_phone_number(self, phone_number):
        self._type(
            self.phone_field,
            phone_number
        )

    def click_phone_next(self):
        self._click(
            self.phone_next_button
        )

    def enter_phone_code(self, code):
        self._type(
            self.phone_code_field,
            code
        )

    # Cartão

    def click_payment_method(self):
        self._click(
            self.payment_method
        )

    def click_add_card(self):
        self._click(
            self.add_card_button
        )

    def enter_card_number(self, card_number):
        self._type(
            self.card_number_field,
            card_number
        )

    def enter_card_code(self, card_code):
        self._type(
            self.card_code_field,
            card_code
        )

    def click_add_card_button(self):
        # Tira o foco do campo CVV.
        # A tarefa informa que o botão "Adicionar"
        # pode permanecer desabilitado enquanto o CVV
        # estiver com foco.
        self.driver.find_element(
            By.TAG_NAME,
            "body"
        ).send_keys("\t")

        self._click(
            self.card_add_button
        )

    # Comentário para o motorista

    def enter_comment(self, comment):
        self._type(
            self.comment_field,
            comment
        )

    # Cobertor

    def click_blanket(self):
        self._click(
            self.blanket_switch
        )

    def is_blanket_selected(self):
        element = self.wait.until(
            EC.presence_of_element_located(
                self.blanket_checked
            )
        )

        return element.is_selected()

    # Sorvete

    def click_ice_cream_plus(self):
        self._click(
            self.ice_cream_plus
        )

    # Modal de busca de carros

    def is_car_search_modal_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.car_search_modal
            )
        ).is_displayed()







