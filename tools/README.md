# Spec Kit Viewer

A small, read-only Streamlit browser for the project's constitution and Spec Kit Markdown files.
It reads the files in place and does not edit, delete, copy, or regenerate them.

## Run on Windows PowerShell

From the repository root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install streamlit
python -m streamlit run tools/spec_viewer.py --server.address 127.0.0.1 --server.port 8501
```

Open `http://127.0.0.1:8501` in a browser. The app is bound to loopback only.

Use **Refresh** after running Spec Kit commands to see newly generated or edited files.
Expected files such as `plan.md`, `research.md`, or `tasks.md` are called out when they
have not been generated yet.

Stop the app with `Ctrl+C` in PowerShell.
