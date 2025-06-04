import requests
from datetime import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1379643507894915102/jUtfOdLN6eXbi7OSjtHM01ae3OrzxyYFsNv4qAPUh6BfQ7XWYuOB_scGZZH7ryCu31cF"

THUMBNAIL_URL = "https://cdn.discordapp.com/attachments/1376607654201524318/1379675803310362664/tgkcred.png?ex=68411ab8&is=683fc938&hm=65e51229cd721cf1099d4ff33e47e2eabb46774f9e1340f1baa82eda7d46362a&"
FOOTER_ICON_URL = "https://cdn.discordapp.com/attachments/1376607654201524318/1379675803310362664/tgkcred.png?ex=68411ab8&is=683fc938&hm=65e51229cd721cf1099d4ff33e47e2eabb46774f9e1340f1baa82eda7d46362a&"

def send_clan_report(players):
    print("Enviando dados para Discord...")

    embeds = []
    for i in range(0, len(players), 10):  # Grupos de 10 jogadores por embed
        embed = {
            "title": f"Relatório do Clã - Jogadores {i + 1} a {min(i + 10, len(players))}",
            "description": "",
            "color": 0xff0000,
            "thumbnail": {
                "url": THUMBNAIL_URL
            },
            "footer": {
                "text": "Relatório diário gerado por cajango-dev (Febbo)",
                "icon_url": FOOTER_ICON_URL
            },
            "timestamp": datetime.utcnow().isoformat()
        }

        for player in players[i:i + 10]:
            embed["description"] += (
                f"**{player['username']}**\n"
                f"Weekly TS: `{player['weekly_ts']}` | "
                f"Weekly TPK: `{player['weekly_tpk']}` | "
                f"Weekly Loots: `{player['weekly_loots']}`\n\n"
            )

        embeds.append(embed)

    for i in range(0, len(embeds), 10):
        chunk = embeds[i:i + 10]
        response = requests.post(WEBHOOK_URL, json={"embeds": chunk})
        if response.status_code != 204:
            print("Erro ao enviar mensagem:", response.status_code, "-", response.text)
        else:
            print(f"Embed(s) {i + 1} a {i + len(chunk)} enviado(s) com sucesso.")
