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

Cloudflare Pages settings:

- Build command: `pip install -r requirements.txt && mkdocs build`
- Build output directory: `site`
- Root directory: leave empty
