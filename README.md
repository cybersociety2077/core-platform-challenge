# Core Platform Challenge

API de Ciber Inteligencia construida con FastAPI.

## Installation

Crea y activa un entorno virtual:

```console
$ python -m venv env
$ .\env\Scripts\Activate.ps1
```

Instala las dependencias:

```console
$ pip install -r requirements.txt
```

## Run it

```console
$ python -m uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Application startup complete.
```

## Try it

Abre tu navegador en <a href="http://127.0.0.1:8000/docs" target="_blank">http://127.0.0.1:8000/docs</a> para ver la documentación interactiva.

Envía una petición:

```console
$ curl -X POST http://127.0.0.1:8000/security/cyber-intelligence -H "Content-Type: application/json" -d "{\"domain\": \"example.com\"}"
```
