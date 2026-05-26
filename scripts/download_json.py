import requests
import math
import time
from pathlib import Path

# =========================
# CONFIGURACIÓN
# =========================

EVENT_ID = 1139503
EVENT_COURSE_ID = 2685622

TOTAL_ATHLETES = 5307
LIMIT = 50

OUTPUT_DIR = Path("data/raw/json")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# =========================
# HEADERS
# =========================

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json,text/plain,*/*",
    "Referer": "https://results.athlinks.com/"
}

# =========================
# DESCARGA
# =========================

pages = math.ceil(TOTAL_ATHLETES / LIMIT)

print("\n======================")
print("INICIANDO DESCARGA")
print("======================\n")

print(f"Total atletas: {TOTAL_ATHLETES}")
print(f"Total páginas: {pages}\n")

for i in range(pages):

    offset = i * LIMIT

    url = (
        f"https://results.athlinks.com/event/{EVENT_ID}"
        f"?eventCourseId={EVENT_COURSE_ID}"
        f"&divisionId="
        f"&intervalId="
        f"&from={offset}"
        f"&limit={LIMIT}"
    )

    print(f"[{i+1}/{pages}] Descargando offset {offset}")

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        output_file = OUTPUT_DIR / f"resultados_{offset}.json"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"OK -> {output_file.name}")

    except Exception as e:

        print(f"ERROR EN OFFSET {offset}")
        print(e)

    time.sleep(0.8)

print("\n======================")
print("DESCARGA COMPLETADA")
print("======================")