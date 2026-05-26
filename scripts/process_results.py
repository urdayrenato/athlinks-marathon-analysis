import json
from pathlib import Path

import pandas as pd

# =========================
# CONFIGURACIÓN
# =========================

RACE_NAME = "21k"

INPUT_FOLDER = Path(f"data/raw/{RACE_NAME}")
OUTPUT_FOLDER = Path("outputs")

OUTPUT_FOLDER.mkdir(exist_ok=True)

# =========================
# LECTURA JSON
# =========================

json_files = sorted(INPUT_FOLDER.glob("*.json"))

print(f"\nArchivos encontrados: {len(json_files)}")

if len(json_files) == 0:
    raise Exception("NO SE ENCONTRARON ARCHIVOS JSON")

all_results = []

# =========================
# PROCESAMIENTO
# =========================

for file in json_files:

    print(f"Procesando: {file.name}")

    try:

        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not data:
            continue

        interval_results = data[0]["interval"]["intervalResults"]

        for runner in interval_results:

            time_millis = (
                runner.get("time", {})
                .get("timeInMillis")
            )

            row = {

                "overall_rank":
                    runner.get("overallRank"),

                "gender_rank":
                    runner.get("genderRank"),

                "age_rank":
                    runner.get("primaryBracketRank"),

                "bib":
                    runner.get("bib"),

                "name":
                    runner.get("displayName"),

                "gender":
                    runner.get("gender"),

                "age":
                    runner.get("age"),

                "country":
                    runner.get("country"),

                "region":
                    runner.get("region"),

                "time_millis":
                    time_millis,
            }

            all_results.append(row)

    except Exception as e:

        print(f"ERROR EN {file.name}")
        print(e)

# =========================
# DATAFRAME
# =========================

df = pd.DataFrame(all_results)

print("\nTOTAL REGISTROS:")
print(len(df))

# eliminar duplicados

df = df.drop_duplicates(
    subset=["overall_rank", "bib", "name"]
)

print("\nTOTAL SIN DUPLICADOS:")
print(len(df))

# =========================
# TIEMPOS
# =========================

df["time_seconds"] = (
    df["time_millis"] / 1000
)

df["time_hms"] = pd.to_timedelta(
    df["time_seconds"],
    unit="s"
).astype(str)

# =========================
# PACE
# =========================

DISTANCE_KM = {
    "10k": 10,
    "21k": 21.097,
    "42k": 42.195
}

distance = DISTANCE_KM[RACE_NAME]

df["pace_min_km"] = (
    df["time_seconds"] / 60 / distance
)

# =========================
# ORDENAMIENTO
# =========================

df = df.sort_values(
    by="overall_rank",
    ascending=True
)

# =========================
# EXPORTACIÓN
# =========================

csv_path = (
    OUTPUT_FOLDER /
    f"{RACE_NAME}_results.csv"
)

excel_path = (
    OUTPUT_FOLDER /
    f"{RACE_NAME}_results.xlsx"
)

df.to_csv(
    csv_path,
    index=False,
    encoding="utf-8-sig"
)

df.to_excel(
    excel_path,
    index=False
)

# =========================
# RESUMEN
# =========================

print("\nCSV GENERADO:")
print(csv_path)

print("\nEXCEL GENERADO:")
print(excel_path)

print("\nTOP 10:")

print(
    df[
        [
            "overall_rank",
            "name",
            "gender",
            "age",
            "time_hms",
            "pace_min_km"
        ]
    ].head(10)
)