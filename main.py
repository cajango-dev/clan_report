from scraper import scrape_clan
from discord_bot import send_clan_report

CLAN_URL = "https://www.dfprofiler.com/clan/view/1405"

def main():
    print("Starting scraping...")
    players = scrape_clan(CLAN_URL)
    print(f"Extracted data: {len(players)} players data.")

    print("Sending to Discord...")
    send_clan_report(players)

if __name__ == "__main__":
    main()
