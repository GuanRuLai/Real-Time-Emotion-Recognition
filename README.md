## 專案介紹
本專案是一個 **即時情緒偵測應用**，透過 `OpenCV` 擷取攝影機影像，並使用 `DeepFace` 進行情緒分析。分析結果會即時顯示在畫面上，且支援 **繁體中文** 顯示情緒類別。

## 功能特點
- **即時影像擷取**：使用 OpenCV 讀取攝影機畫面。
- **情緒分析**：透過 DeepFace 分析人臉情緒。
- **繁體中文顯示**：偵測到的情緒將以 **繁體中文** 呈現。
- **支援七種情緒**：
  - 生氣 (`angry`)
  - 噁心 (`disgust`)
  - 害怕 (`fear`)
  - 開心 (`happy`)
  - 難過 (`sad`)
  - 驚訝 (`surprise`)
  - 正常 (`neutral`)

## 安裝與使用
### 1. 安裝必要的套件
請確保你的環境安裝了以下 Python 套件：
```bash
pip install opencv-python deepface numpy pillow
```

### 2. 下載中文字型
此專案使用 **Noto Sans TC** 字型來顯示繁體中文，請先下載字型並放置於專案資料夾內：
- [Noto Sans TC 下載](https://fonts.google.com/noto/specimen/Noto+Sans+TC)

### 3. 執行程式
```bash
python emotion_detection.py
```

按 `q` 鍵可退出程式。

## 技術細節
### 1. **即時影像擷取**
- 使用 `cv2.VideoCapture(0)` 開啟攝影機。
- 透過 `cv2.resize()` 進行影像縮放。

### 2. **情緒分析**
- 使用 `DeepFace.analyze(img, actions=["emotion"])` 分析影像。
- 取得 **dominant_emotion** 作為主要情緒。

### 3. **中文顯示**
- 透過 `PIL.ImageFont` 載入 `NotoSansTC-VariableFont_wght.ttf`。
- 使用 `PIL.ImageDraw` 在影像上繪製文字。

## 授權條款
本專案採用 **MIT License**，允許自由使用與修改，惟請保留原始授權條款。
