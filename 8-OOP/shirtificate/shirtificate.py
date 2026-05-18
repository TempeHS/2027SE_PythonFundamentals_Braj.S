from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 40)
    pdf.cell(0, 45, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.image("shirtificate.png", x=10, y=70, w=190)

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)

    pdf.set_y(120)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
