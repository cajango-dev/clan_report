from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

    rank_order = {
        "K I N G C R O W": 1,
        "Governor Crow": 2,
        "Legend Crow": 3,
        "Night Crow": 4,
        "Military Crow": 5,
        "Not Compete": 6
    }

    # Primeiro coletar dados básicos
    rows = driver.find_elements(By.CSS_SELECTOR, "table.table > tbody > tr")
    players = []
    not_compete_players = []

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 8:
            username = cols[1].text.strip()
            rank = cols[3].text.strip()
            weekly_ts = cols[5].text.strip()
            weekly_tpk = cols[6].text.strip()
            weekly_loots = cols[7].text.strip()

            player_data = {
                "username": username,
                "rank": rank,
                "weekly_ts": weekly_ts,
                "weekly_tpk": weekly_tpk,
                "weekly_loots": weekly_loots,
                "profile_link": None
            }

            if rank.strip().lower() == "not compete":
                # pegar link para acessar depois
                try:
                    profile_link = cols[1].find_element(By.TAG_NAME, "a").get_attribute("href")
                    player_data["profile_link"] = profile_link
                    not_compete_players.append(player_data)
                except Exception as e:
                    print(f"[!] Erro ao pegar link do perfil de {username}: {e}")

            players.append(player_data)

    # Agora, para os Not Compete, acessar perfil individual e atualizar dados
    for player in not_compete_players:
        try:
            driver.get(player["profile_link"])
            time.sleep(3)

            player["weekly_ts"] = driver.find_element(By.XPATH, '//*[@id="view-profile"]/div[2]/div[1]/div/div[2]/div/div[1]/div/div').text.strip()
            player["weekly_tpk"] = driver.find_element(By.XPATH, '//*[@id="view-profile"]/div[2]/div[2]/div/div[2]/div/div[2]/div/div').text.strip()
            player["weekly_loots"] = driver.find_element(By.XPATH, '//*[@id="view-profile"]/div[2]/div[3]/div/div[2]/div/div[1]/div/div').text.strip()

        except Exception as e:
            print(f"[!] Erro ao buscar dados individuais de {player['username']}: {e}")

    driver.quit()

    # Ordena por rank
    players.sort(key=lambda p: rank_order.get(p["rank"], 999))

    return players
