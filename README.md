# 🗼 Lighthouse

A guided, interactive troubleshooting and learning tool for Arch Linux.

Lighthouse helps you diagnose common Arch Linux issues step by step, using clear questions and explanations instead of guesswork, forum hopping, or endless wiki tabs.

It doesn’t auto-fix your system.
It helps you understand what’s wrong and why — then guides you toward the right solution.

---

## ✨ Features

- 🔍 Interactive troubleshooting flows  
  Step-by-step questions guide you to relevant actions and explanations.

- 🧭 Arch philosophy aligned  
  No automation, no magic — just guidance, commands, and understanding.

- 📚 Searchable knowledge base  
  Quickly find guides by keyword, topic, or category.

- 🧪 Validated flow structure  
  Guides are checked for structural correctness to avoid dead ends.

- 🖥️ Clean terminal UI  
  Minimal, readable, and distraction-free.

---

## 🚀 Getting Started

### Requirements

- Python 3.10+
- Arch Linux (recommended, but not strictly required)
- pyYAML 6.0
- pydantic 2.0
- pytest 8.0

---

## 🛣️ Roadmap

### v1

 - Core CLI

 - Interactive flows

 - Search & help

 - Validator

### v2 (planned)

 - Enforce full validation on all flows

 - Normalize legacy guides

 - Better categorization & metadata

 - Optional TUI enhancements

---

## 🌟 Philosophy

Lighthouse does not fix your system for you.
It helps you understand why something broke — and how to fix it correctly.

“Stop guessing. Start understanding.”

---

### Run Lighthouse

```bash
python cli.py
