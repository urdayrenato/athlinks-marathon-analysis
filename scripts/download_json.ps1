# =========================
# ATHLINKS JSON DOWNLOADER
# =========================

# Carpeta destino
$carpeta = ".\data\raw\json"

# Crear carpeta si no existe
New-Item -ItemType Directory -Force -Path $carpeta

# Parámetros evento
$eventId = 447223
$eventCourseId = 668417

# Configuración paginación
$limit = 50
$totalAthletes = 1773

# Calcular páginas necesarias
$maxPaginas = [math]::Ceiling($totalAthletes / $limit)

Write-Host ""
Write-Host "============================="
Write-Host "INICIANDO DESCARGA JSON"
Write-Host "============================="
Write-Host ""

for ($i = 0; $i -lt $maxPaginas; $i++) {

    $from = $i * $limit

    $url = "https://results.athlinks.com/event/$eventId?eventCourseId=$eventCourseId&divisionId=&intervalId=&from=$from&limit=$limit"

    $archivo = "$carpeta\resultados_$from.json"

    Write-Host "Descargando registros desde: $from"

    try {

        Invoke-WebRequest `
            -Uri $url `
            -OutFile $archivo `
            -Headers @{
                "User-Agent" = "Mozilla/5.0"
            }

        Write-Host "OK -> resultados_$from.json"

    }
    catch {

        Write-Host "ERROR EN OFFSET $from"

    }

    Start-Sleep -Milliseconds 700
}

Write-Host ""
Write-Host "============================="
Write-Host "DESCARGA COMPLETADA"
Write-Host "============================="