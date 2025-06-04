from scraper import scrape_clan
from discord_bot import send_clan_report

CLAN_URL = "https://www.dfprofiler.com/clan/view/1405"

def main():
    print("Iniciando scraping...")
    players = scrape_clan(CLAN_URL)
    print(f"Dados extraídos: {len(players)} jogadores encontrados.")

    print("Enviando dados para Discord...")
    send_clan_report(players)

if __name__ == "__main__":
    main()
