import cv2
from deepface import DeepFace
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# define the Chinese character of the emotion
text_obj = {
    "angry": "生氣",
    "disgust": "噁心",
    "fear": "害怕",
    "happy": "開心",
    "sad": "難過",
    "surprise": "驚訝",
    "neutral": "正常"
}

# define a function to add text
def putText(x, y, text, size=50, color=(0, 0, 0)):
    global img
    fontpath = "NotoSansTC-VariableFont_wght.ttf"            
    font = ImageFont.truetype(fontpath, size)      
    imgPil = Image.fromarray(img) # convert original image into PIL image
    draw = ImageDraw.Draw(imgPil) # build drawing object
    draw.text((x, y), text_obj[text], fill=color, font=font) 
    img = np.array(imgPil) # convert PIL image into numpy array
    
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read() 
    if not ret:
        print("Cannot receive frame") 
        break 
    
    img = cv2.resize(frame, (384, 240))                         
    
    try:
        analyze = DeepFace.analyze(img, actions=["emotion"]) 
        result = analyze[0]
        emotion = result.get("dominant_emotion", "neutral")
        putText(0, 40, emotion)     
    except Exception as e:
        print(f"分析失敗：{e}")
        
    cv2.imshow("Emotion Result", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()		    