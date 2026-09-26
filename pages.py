from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:

    # Seção De e Para
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Fluxo de chamada de táxi
    taxi_option = (By.XPATH, '//button[contains(text(),"Chamar")]')

    # Plano Comfort
    comfort_icon = (By.XPATH, '//img[contains(@src,"kids")]')

    # Plano Comfort selecionado
    comfort_active = (
        By.XPATH,
        '//img[contains(@src,"kids")]/ancestor::*[contains(@class,"active")]'
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Métodos POM

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
            EC.visibility_of_element_located(self.comfort_active)
        )

        print("ELEMENTO ENCONTRADO:", active_button)
        print("CLASSE:", active_button.get_attribute("class"))

        return "active" in active_button.get_attribute("class")







