# AEGIS Capture Windows

Desktop app that drags a region over your MT5 chart, captures screenshots every 3s, and sends to AEGIS cloud for BUY/SELL signals.

## 1. Install
Download Python 3.10+ from python.org

## 2. Build EXE
```bash
pip install -r requirements.txt
pyinstaller aegis_capture.spec
