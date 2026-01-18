import sys

USE_COLOR = sys.stdout.isatty()

def c(code):
    return f"\033[{code}]m" if USE_COLOR else ""
    
RESET = c("0")
BOLD = c("1")

GREEN = c("32")
YELLOW = c("33")
RED = c("31")
BLUE = c("34")
DIM = c("2")

ICON_OK = "✓" if USE_COLOR else "+"
ICON_WARN = "⚠" if USE_COLOR else "!"
ICON_INFO = "ℹ" if USE_COLOR else "i"
