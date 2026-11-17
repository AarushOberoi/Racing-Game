# 🧮 Calculator

A calculator written in **Python** that runs entirely in the browser, with an iPhone-style (Apple Calculator) block interface.

🔗 **Live site:** https://calculator.aarushoberoi.workers.dev

---

## ✨ Features

- **Python-powered**: the calculation logic is real Python, executed in the browser (no server needed)
- **iPhone-style interface**: familiar block layout with round keys
- **Full basic keypad**
  - Digits `0–9` and decimal point `.`
  - Operators `+`, `−`, `×`, `÷`
  - `C` (clear), `±` (toggle sign), `%` (percentage)
  - `=` to evaluate
- **Full-screen layout** that adapts to the viewport, including mobile (`viewport-fit=cover`)
- **Static deployment** on Cloudflare Workers

## 🗂️ Project Structure

```
Calculator/
├── index.html            # Website: calculator UI, loads Python in the browser
└── Requirements/
    ├── Calculation.py    # Calculation logic
    ├── Dashboard.py      # Calculator dashboard/interface logic
    └── Calculator_1.ipynb  # Original notebook version
```

## 🚀 Run Locally

Clone the repo and serve the folder with any static server (opening `index.html` directly may not work, because the browser needs to load Python files over HTTP):

```bash
git clone https://github.com/AarushOberoi/Calculator.git
cd Calculator

# Option 1: Python
python -m http.server 8000

# Option 2: Node
npx serve .
```

Then open `http://localhost:8000`.

To use the original notebook instead:

```bash
jupyter notebook Requirements/Calculator_1.ipynb
```

## ☁️ Deployment

Deployed as static assets on **Cloudflare Workers**:

```bash
npx wrangler deploy
```

## 🧠 How It Works

1. The page loads and initialises a Python runtime in the browser.
2. Button presses on the keypad are passed to the Python calculation logic.
3. The result is shown on the display.

## 🤝 Contributing

Suggestions and pull requests are welcome:

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes and open a pull request

## 👤 Author

Made by [Aarush Oberoi](https://github.com/AarushOberoi)
