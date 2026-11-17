# 🏎️ Endless Racing Game!

An endless car racing game built with **Python** and **pygame**, running right in your browser. Steer your car, dodge the oncoming traffic, and see how long you can survive.

🔗 **Play now:** https://racinggame.aarushoberoi.workers.dev

---

## 🎮 How to Play

1. Open the [live site](https://racinggame.aarushoberoi.workers.dev) and wait for Python and pygame to load.
2. Click **Start Game**.
3. Use the **← Left** and **→ Right** arrow keys to steer.
4. Avoid the enemy cars for as long as you can.

## ✨ Features

- **Real Python game**: the actual pygame code runs in the browser, with no JavaScript rewrite
- **Endless gameplay** on a scrolling road
- **Enemy cars** to dodge
- **Background music**
- **Full-page layout** that fills the whole browser window
- **No install needed**: just open the link and play

## 🗂️ Project Structure

```
Racing-Game/
├── index.html                  # Web page that loads Python + pygame and launches the game
├── Endless_Racing_Game.ipynb   # Original notebook version of the game
├── car.png                     # Player car sprite
├── enemy_car.png               # Enemy car sprite
├── road.png                    # Road background
├── music.mp3                   # Background music
└── *.png                       # Additional image assets
```

## 🚀 Run Locally

### In the browser

Serve the folder with any static server (opening `index.html` directly may not work, because the browser needs to load the assets over HTTP):

```bash
git clone https://github.com/AarushOberoi/Racing-Game.git
cd Racing-Game

# Option 1: Python
python -m http.server 8000

# Option 2: Node
npx serve .
```

Then open `http://localhost:8000`.

### As a desktop game

```bash
pip install pygame jupyter
jupyter notebook Endless_Racing_Game.ipynb
```

## ☁️ Deployment

Deployed as static assets on **Cloudflare Workers**:

```bash
npx wrangler deploy
```

## 🧠 How It Works

1. The page loads a Python runtime with pygame support in the browser.
2. The game's Python code and its assets (images, music) are loaded.
3. Clicking **Start Game** runs the game loop, drawing to a canvas that fills the page.

## 🛠️ Built With

- Python
- pygame
- HTML / CSS
- Cloudflare Workers (hosting)

## 🤝 Contributing

Ideas and pull requests are welcome:

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes and open a pull request

## 👤 Author

Made by [Aarush Oberoi](https://github.com/AarushOberoi)
