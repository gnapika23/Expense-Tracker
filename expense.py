class Expense:
    def __init__(self, name, category, amount) -> None:  # Corrected method name
        self.name = name
        self.category = category
        self.amount = amount  # Fixed spacing
    def __repr__(self):
        return f"<Expense : {self.name} , {self.category} , ${self.amount:.2f} >"