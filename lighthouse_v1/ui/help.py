from ui.render import section, text

def show_help():
    section("Lighthouse Help")

    text("Lighthouse is an interactive CLI for learning and troubleshooting Linux,")
    text("inspired by the Arch Wiki and Arch philosophy.\n")

    text("Main options:")
    text("  l  List available guides")
    text("  r  Run a guide")
    text("  s  Search guides by keyword")
    text("  h  Show this help")
    text("  q  Quit\n")

    text("Guides are interactive decision trees.")
    text("They do not make changes to your system.")

    section("Inside guides")
    text("- Type the letter shown in [brackets] and press Enter")
    text("- Press Ctrl+C or type 'q' to quit at any time")

   

    section("Philosophy")
    text("Lighthouse follows Arch Linux principles:")
    text("- Minimal")
    text("- Explicit")
    text("- User-controlled")

