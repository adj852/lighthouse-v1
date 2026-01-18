import sys

ANSI_ENABLED = sys.stdout.isatty()

WIDTH = 70
LEFT_PAD = 2


def color(code, text):
    if not ANSI_ENABLED:
        return text
    return f"\033[{code}m{text}\033[0m"


def _line(char="="):
    return char * WIDTH


def _center(text):
    return text.center(WIDTH)


def header(title, subtitle=None):
    print(color("1", _line("=")))
    print(color("1", _center(title)))
    if subtitle:
        print(color("1", _center(subtitle)))
    print(color("1", _line("=")))


def divider():
    print(color("2", _line("-")))


def section(text):
    print()
    print(" " * LEFT_PAD + color("1", text))


def option(key, text):
    print(" " * LEFT_PAD + f"[{key}] {text}")


def info(text):
    print(" " * LEFT_PAD + color("36", f"ℹ {text}"))


def warn(text):
    print(" " * LEFT_PAD + color("33", f"⚠ {text}"))


def success(text):
    print(" " * LEFT_PAD + color("32", f"✓ {text}"))


def text(text):
    print(" " * LEFT_PAD + text)

def list_item(key, title, category):
    print(f"- {key:15} {title} [{category}]")

def prompt():
    try:
        return input("> ").strip()
    except KeyboardInterrupt:
        print()
        return "q"

