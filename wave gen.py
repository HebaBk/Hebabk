from playsound import playsound
import threading

def play_success():
    playsound("success.mp3")

# تشغيل الصوت في thread مستقل
thread = threading.Thread(target=play_success)
thread.start()

print("✅ Sound is playing asynchronously...")
