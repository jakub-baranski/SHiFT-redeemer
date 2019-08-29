class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver
        super().__init__()