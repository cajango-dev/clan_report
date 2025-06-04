from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # <- ESSA LINHA
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def scrape_clan(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(5)

    players = []

    # Defina a ordem dos ranks
    rank_order = {
        "K I N G C R O W": 1,
        "Governor Crow": 2,
        "Legend Crow": 3,
        "Night Crow": 4,
        "Military Crow": 5,
        "Not Compete": 6
    }

    rows = driver.find_elements(By.CSS_SELECTOR, "table.table > tbody > tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 8:
            username = cols[1].text.strip()
            rank = cols[3].text.strip()
            weekly_ts = cols[5].text.strip()
            weekly_tpk = cols[6].text.strip()
            weekly_loots = cols[7].text.strip()

            players.append({
                "username": username,
                "rank": rank,
                "weekly_ts": weekly_ts,
                "weekly_tpk": weekly_tpk,
                "weekly_loots": weekly_loots
            })

    driver.quit()

    # Ordena pela hierarquia
    players.sort(key=lambda p: rank_order.get(p["rank"], 999))

    return players
