# Athlinks Marathon Analysis

Proyecto de extracción y análisis de resultados de carreras desde Athlinks utilizando Python.

## Objetivo

Construir un pipeline simple de ingeniería de datos para:

- extraer resultados de carreras
- procesar archivos JSON
- transformar datos estructurados
- generar datasets analíticos en CSV y Excel

El proyecto nació como iniciativa personal para analizar resultados de running (10K, 21K y 42K), aplicando conceptos de automatización, ETL y analytics.

---

## Tecnologías utilizadas

- Python
- Requests
- Pandas
- PowerShell
- JSON APIs
- Git / GitHub

---

## Funcionalidades

### 1. Descarga automatizada de resultados

El script identifica y consume endpoints JSON utilizados por Athlinks para paginar resultados oficiales de carrera.

Características:

- descarga paginada
- extracción masiva de resultados
- manejo de offsets
- exportación JSON raw

---

### 2. Transformación y limpieza de datos

Procesamiento de:

- rankings generales
- categoría
- género
- edad
- tiempos oficiales
- pace por kilómetro

Incluye:

- eliminación de duplicados
- normalización temporal
- exportación CSV/XLSX

---

## Estructura del proyecto

```text
athlinks-marathon-analysis/
│
├── data/
│   └── raw/
│       ├── 21k/
│       └── 42k/
│
├── outputs/
│
├── scripts/
│   ├── download_json.py
│   └── process_results.py
│
├── requirements.txt
└── README.md
```

---

## Ejemplo de uso

### Descargar resultados

```bash
python scripts/download_json.py
```

### Procesar resultados

```bash
python scripts/process_results.py
```

---

## Aprendizajes aplicados

Este proyecto integra conceptos de:

- automatización de procesos
- ingeniería ligera de datos
- ETL
- consumo de APIs
- análisis exploratorio
- parametrización de pipelines
- estructuración de datasets

---

## Autor

Renato Urday Calcina

Ingeniero Industrial | Analista y Arquitecto de Procesos | Running & Data Analytics