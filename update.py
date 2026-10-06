import urllib.request
from pathlib import Path

SOURCES = [
    ("Fulgione", "https://davidefulgione.com/tv.m3u"),
    ("Tundrak", "https://raw.githubusercontent.com/Tundrak/IPTV-Italia/main/iptvita.m3u"),
    ("Tundrak Plus", "https://raw.githubusercontent.com/Tundrak/IPTV-Italia/main/iptvitaplus.m3u"),
    ("sfiorini", "https://raw.githubusercontent.com/sfiorini/IPTV-Italy/main/iptvitaly.m3u"),
    ("OpenIPTVItaly", "https://raw.githubusercontent.com/xN1ckuz/OpenIPTVItaly/main/OpenIPTVItaly.m3u"),
    ("TVITALIA", "https://raw.githubusercontent.com/maginetweb-arch/TVITALIA/main/iptvit.m3u"),
    ("vise950", "https://raw.githubusercontent.com/vise950/iptv_italy/main/italy.m3u"),
]

OUTPUT = Path("playlist.m3u")


def download(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


result = ["#EXTM3U"]

for name, url in SOURCES:
    try:
        content = download(url)

        lines = content.splitlines()

        # Mantiene tutti i canali e tutti i doppioni.
        # Rimuove soltanto l'intestazione #EXTM3U delle singole playlist.
        result.append(f"# --- {name} ---")

        for line in lines:
            if line.strip() != "#EXTM3U":
                result.append(line)

        print(f"OK: {name}")

    except Exception as e:
        print(f"ERRORE: {name}: {e}")

OUTPUT.write_text("\n".join(result) + "\n", encoding="utf-8")

print("Playlist aggregata creata.")
