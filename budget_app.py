class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23].ljust(23)
            amt = f"{entry['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate total withdrawals per category
    spend = []
    for category in categories:
        total = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spend.append(total)
    total_spent = sum(spend)
    
    # Calculate percentages (rounded down to nearest 10)
    percentages = [int((s / total_spent) * 100 // 10 * 10) for s in spend]

    lines = ["Percentage spent by category"]
    
    # Chart bars
    for i in range(100, -1, -10):
        line = str(i).rjust(3) + "|"
        for perc in percentages:
            line += " o " if perc >= i else "   "
        lines.append(line + " ")

    # Horizontal line
    lines.append("    " + "-" * (len(categories) * 3 + 1))

    # Vertical category names
    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += category.name[i] + "  "
            else:
                line += "   "
        lines.append(line)

    return "\n".join(lines)