# DFProfiler Clan Report Bot

A Python-based bot that scrapes weekly performance stats from the [DFProfiler](https://www.dfprofiler.com/) clan pages and posts a structured report to a Discord channel using webhooks.

## 🚀 Features

- Scrapes the following weekly statistics for each clan member:
  - Total Score (TS)
  - Player Kills (TPK)
  - Loots Collected
- Handles members marked as "Not Compete" by visiting their individual profile pages.
- Posts rich, paginated embeds to Discord with customized server emojis.
- Uses `selenium` with `webdriver-manager` for easy automation.
- Headless scraping (does not open a browser window).
  
## 📦 Requirements

- Python 3.8+
- Google Chrome installed

Install dependencies:

```bash
pip install -r requirements.txt
```

Note: Ensure chromedriver matches your Chrome version (managed automatically via webdriver-manager).

⚙️ Setup
Clone the repository:
```
git clone https://github.com/your-username/dfprofiler-clan-report.git
cd dfprofiler-clan-report
```
Configure the webhook URL:

In scraper.py or webhook_sender.py, set:
```
WEBHOOK_URL = "https://discord.com/api/webhooks/..."
```

🧪 Running
Run the bot via:
```
python main.py
```
This will:

Scrape all player stats from the specified clan page.

Compose paginated embeds.

Send the results to the configured Discord webhook.

File Structure: 
.
├── main.py               # Entry point script

├── scraper.py            # Contains logic for scraping DFProfiler

├── webhook_sender.py     # (Optional) Handles sending embeds to Discord

├── requirements.txt      # Python dependencies

└── README.md             # You're here!

🛡️ Disclaimer
This project is not affiliated with DFProfiler or its developers. Use responsibly and avoid excessive scraping.

🙌 Credits
Developed by cajango-dev (Febbo)
Special thanks to the DFProfiler and Dead Frontier communities.
