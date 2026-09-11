# GWB Wiki

Personal wiki built with Material for MkDocs and intended for Cloudflare Pages.

## Local preview

```powershell
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Open <http://127.0.0.1:8000/>.

## Build

```powershell
python -m mkdocs build
```

Before building after adding or correcting China Cloud Atlas figure entries, refresh the random cloud catalog:

```powershell
python tools/build_random_cloud_catalog.py
```

Cloudflare Pages settings:

- Build command: `pip install -r requirements.txt && mkdocs build`
- Build output directory: `site`
- Root directory: leave empty
