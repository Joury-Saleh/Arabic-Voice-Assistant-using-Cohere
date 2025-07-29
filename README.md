#  Arabic Voice Assistant using Cohere & gTTS


This project is a smart **Arabic voice assistant** built with:

-  Speech recognition using Google Speech Recognition
-  Smart response generation using [Cohere LLM API](https://cohere.com/)
-  Arabic text-to-speech using `gTTS`
-  Audio playback using `pygame`
-  Continuous voice interaction until you say: **"توقف"**

---

##  Features

-  Arabic speech input
-  Smart replies from a language model
-  Voice response in Arabic
-  Conversation loop
-  Conversation history saved in `text.txt`

---

## 🛠️ Installation

```bash
pip install cohere gTTS pygame SpeechRecognition
```

## API Key Setup

- Sign up at [cohere](https://cohere.com/)
- Go to API Keys and copy your key
- Replace the following line in the code:
```py
co = cohere.Client('YOUR_COHERE_API_KEY')
```

## How It Works

1- The assistant greets you in Arabic
2- Listens to your voice
3- Converts your speech to text
4- Sends it to Cohere for a smart reply
5- Speaks the reply using```gTTS```
6- Repeats the loop until you say: "توقف", "خلاص", or "إنهاء"

## Sample Result

###Example Interaction

```
Assistant: السلام عليكم، أنا مساعدك الذكي، قل لي كيف أساعدك، وعندما تنتهي قل: توقف.

📢 تحدث الآن...
🗣️ أنت قلت: ما الفرق بين المبرمج والمصمم؟
🤖 الرد: المصمم يبتكر الواجهة، بينما المبرمج يطور الوظيفة.

```


![screenshot](screenshot.png)

## Notes
- Make sure your microphone is connected and working
- Uses pygame instead of playsound for better compatibility.
- 
