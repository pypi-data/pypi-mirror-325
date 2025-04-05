class ftnick_core:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hello from {self.name}, powered by ftnick_core!"

    def farewell(self) -> str:
        return f"Goodbye from {self.name}, see you next time!"
