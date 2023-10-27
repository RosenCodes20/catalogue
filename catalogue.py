class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.product_name = product_name
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        self.given_letter = []
        for x in self.products:
            if x.startswith(first_letter):
                self.given_letter.append(x)
        return self.given_letter

    def __repr__(self):
        self.result = ""
        self.result += f"Items in the {self.name} catalogue:\n"
        self.result += "\n".join(sorted(self.products))
        return self.result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
