from fpdf import FPDF

class ShirtificatePDF(FPDF):
    
    def __init__(self, name):
        super().__init__()

        self.name = name
        
        self.add_page()

        self.set_font("helvetica", "B", size=52)
        self.cell(0, 20, "CS50 Shirtificate", align="C")
        self.ln(20)

        self.image("shirtificate.png", w=self.epw)

    def make_shirt(self):
        text = f"{self.name} took CS50"

        self.set_font("helvetica", size=24)
        self.set_text_color(255, 255, 255)

        self.set_y(140)
        self.cell(0, 10, text, align="C")

        self.output("shirtificate.pdf")


def main():
    name = input("Name: ")
    pdf = ShirtificatePDF(name)
    pdf.make_shirt()


if __name__ == "__main__":
    main()