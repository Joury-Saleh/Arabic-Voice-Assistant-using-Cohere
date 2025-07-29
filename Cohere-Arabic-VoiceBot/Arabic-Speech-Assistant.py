import cohere
from gtts import gTTS
import pygame
import os
import speech_recognition as sr

# تهيئة Cohere
co = cohere.Client('YOUR_COHERE_API_KEY')  # ← ضع مفتاح API الصحيح هنا

# تهيئة التعرف على الصوت
r = sr.Recognizer()

# دالة لتشغيل الصوت باستخدام pygame
def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.quit()

# دالة لحذف ملف صوتي إذا كان موجوداً
def safe_remove(file_path):
    if os.path.exists(file_path):
        try:
            pygame.mixer.quit()
            os.remove(file_path)
        except Exception as e:
            print("⚠️ لم يمكن حذف الملف:", e)

# تشغيل الترحيب الصوتي
intro = "السلام عليكم، أنا مساعدك الذكي، قل لي كيف أساعدك، وعندما تنتهي قل: توقف."
print("Assistant:", intro)
safe_remove("intro.mp3")
gTTS(text=intro, lang='ar').save("intro.mp3")
play_audio("intro.mp3")

# بدء الحلقة الرئيسية
while True:
    try:
        with sr.Microphone() as src:
            print("\n📢 تحدث الآن...")
            audio = r.listen(src)

        # تحويل الصوت إلى نص
        user_text = r.recognize_google(audio, language='ar-SA')
        print("🗣️ أنت قلت:", user_text)

        # حفظ النص في ملف
        with open('text.txt', 'a', encoding='utf-8') as f:
            f.write("User: " + user_text + '\n')

        # التحقق من أمر الإيقاف
        if any(word in user_text.lower() for word in ['توقف', 'خلاص', 'انهاء']):
            bye = "تم الإيقاف. إلى اللقاء!"
            print("Assistant:", bye)
            safe_remove("bye.mp3")
            gTTS(text=bye, lang='ar').save("bye.mp3")
            play_audio("bye.mp3")
            break

        # توليد الرد من Cohere
        response = co.generate(
            model='command-r-plus',
            prompt=f'رد باختصار وبأسلوب مساعد ذكي على: {user_text}',
            max_tokens=100,
            temperature=0.7,
        )
        reply_text = response.generations[0].text.strip()
        print("🤖 الرد:", reply_text)

        # حفظ الرد في الملف
        with open('text.txt', 'a', encoding='utf-8') as f:
            f.write("Assistant: " + reply_text + '\n')

        # إنشاء الملف الصوتي للرد
        safe_remove("response.mp3")
        gTTS(text=reply_text, lang='ar').save("response.mp3")
        play_audio("response.mp3")

    except sr.UnknownValueError:
        print("⚠️ لم يتم التعرف على الصوت، حاول مرة أخرى.")
    except sr.RequestError as e:
        print(f"⚠️ خطأ في خدمة Google: {e}")
    except cohere.CohereError as e:
        print(f"⚠️ خطأ Cohere: {e}")
    except Exception as e:
        print("⚠️ حدث خطأ غير متوقع:", e)
