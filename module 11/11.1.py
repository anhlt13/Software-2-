class Publication:
    def __init__(self,name):
        self.name = name

    def print_inf(self):
        print(f"This publication is about: {self.name}")

class Magazine(Publication):
    def __init__(self,name , chief_editor):
        super().__init__("Aki")
        self.name = name
        self.chief_editor = chief_editor

    def print_inf(self):
        super().print_inf()
        print(f" (chief editor {self.chief_editor})")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__("Compartment No.6")
        self.author = author
        self.page_count = page_count

    def print_inf(self):
        super().print_inf()
        print(f" - Author {self.author}, {self.page_count} pages")


publication = Publication("Donald Duck")
publication.print_inf()

magazine = Magazine("Aki","Aki Hyyppa")
magazine.print_inf()

book = Book("Compartment No.6","Rosa Liksom", 192)
book.print_inf()