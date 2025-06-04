import requests
from datetime import datetime

WEBHOOK_URL = ""

THUMBNAIL_URL = ""
FOOTER_ICON_URL = ""

def send_clan_report(players):
    print("Enviando dados para Discord...")

    embeds = []
    for i in range(0, len(players), 10):  # Group of 10 members for embed
        embed = {
            "title": f"Clan Report - Players {i + 1} a {min(i + 10, len(players))}",
            "description": "",
            "color": 0x00adff,
            "thumbnail": {
                "url": THUMBNAIL_URL
            },
            "footer": {
                "text": "Made by cajango-dev",
                "icon_url": FOOTER_ICON_URL
            },
            "timestamp": datetime.utcnow().isoformat()
        }

        for player in players[i:i + 10]:
            is_not_compete = player["rank"].strip().lower() == "not compete"
            emoji = "🔴" if is_not_compete else "🟢"
            name = f"{emoji} **{player['username']}**"

            embed["description"] += (
                f"{name}\n"
                f"Weekly TS: `{player['weekly_ts']}` | "
                f"Weekly TPK: `{player['weekly_tpk']}` | "
                f"Weekly Loots: `{player['weekly_loots']}`\n\n"
            )

        embeds.append(embed)

    for i in range(0, len(embeds), 10):
        chunk = embeds[i:i + 10]
        response = requests.post(WEBHOOK_URL, json={"embeds": chunk})
        if response.status_code != 204:
            print("Erro when message sent:", response.status_code, "-", response.text)
        else:
            print(f"Embed(s) {i + 1} a {i + len(chunk)} has succesfully sent!")
