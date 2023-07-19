import openpyxl as excelExcelHaiExcelExcelHaiIskiSafediKaJawaabNahi
import time 
import winsound
import pyttsx3


wb = excelExcelHaiExcelExcelHaiIskiSafediKaJawaabNahi.load_workbook('PLX-DAQ-v2-AutoGrapher-RandomValue.xlsm')
ws = wb.active


engine = pyttsx3.init('sapi5')

def speakSomething(x):
    engine.setProperty('rate', 150)  
    engine.setProperty('volume', 0.8)  
    engine.say(x)
    engine.runAndWait()

def greetTheListener():
    currentTime = time.localtime().tm_hour
    if currentTime < 12:
        speakSomething("Good Morning Everyone!")
    elif currentTime > 12 and currentTime < 16:
        speakSomething("Good Afternoon Everyone!")
    else:
        speakSomething("Good Evening Everyone!")
                                                            
for row in ws.iter_rows(min_row=1, values_only=True):
    row_value = row[2]
    print(row_value)
    time.sleep(1)


    def mainMethod():
        if row_value == "Roshan" or row_value == "Sanku" or row_value == "Karan" or row_value == "Ritesh":

            duration = 10

            start_time = time.time()
            print("Timer started...")

            while time.time() - start_time < duration:
                time.sleep(1)

            # Toon Toon
            frequency = 2000 
            duration_ms = 1000
            winsound.Beep(frequency, duration_ms)

            print("Timer finished!")

            engine = pyttsx3.init()

            def speakSomething(x):
                engine.setProperty('rate', 150)  
                engine.setProperty('volume', 0.8)  
                engine.say(x)
                engine.runAndWait()

            greetTheListener()
            speakSomething(f"Important Announcement, {row_value} to report to his class immediately.")

    if row_value is None:
        break

    else:
        mainMethod()




