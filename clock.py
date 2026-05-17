import time
import os
"""
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
print("🕛 Live Terminal Clock")
print("Press CTRL+C to stop\n")

try:
    while True:
        clear()
        current = time.localtime()

        hours = str(current.tm_hour).zfill(2)
        minutes = str(current.tm_min).zfill(2)
        seconds = str(current.tm_sec).zfill(2)

        date = time.strftime("%A, %B %d %Y")

        print("=" * 30)
        print(f" 🕛 {hours} : {minutes} : {seconds} ")
        print("=" * 30)
        print(f" 📆 {date}")
        print("=" * 30)

        time.sleep(1)

except KeyboardInterrupt:
    print("\n⏰ Clock stopped.")