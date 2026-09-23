# GG-Capacity · 台積電產能版圖

台積電全球晶圓廠與先進封裝廠的逐廠、逐期盤點，內容包括製程節點、產能、量產時程，以及晶圓、CoWoS、SoIC 的產能演進圖表。

> **本網站資料由 AI 自動收集、整理與推估，不代表台積電（TSMC）官方實際資料，僅供研究參考，不構成投資建議。**

## 檔案

| 檔案 | 用途 |
|---|---|
| `page.html` | 唯一的原始檔，所有資料集中在 `<script>` 裡的 `DATA` 區塊 |
| `build.py` | 由 `page.html` 產生 `index.html`（加上完整 HTML 骨架與 Google tag） |
| `index.html` | GitHub Pages 發布的頁面，由程式產生，請勿手動修改 |

## 更新流程（每週自動執行）

1. 搜尋台積電新廠、產能、封裝的最新消息，修改 `page.html` 的 `DATA` 區塊（`SITES`、`BENCH`、`SOURCES`、`CHANGELOG`、`META`）。
2. 執行 `python build.py`。
3. commit 並 push 到 `main`，GitHub Pages 會自動重新部署。
