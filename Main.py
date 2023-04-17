# Import Required Library
from tkinter import *
from threading import *
import datetime
import time
import winsound

# Create object
window = Tk()

# Set the geometry
window.geometry("400x300")

# Use threading
def Threading():
   t1 = Thread(target=alarm)
   t1.start()

def alarm():
   # Infinity loop
   while True:
      # Set Alarm
      set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"

      # Waite for 1 sec
      time.sleep(1)

      # Get curent time
      curent_time = datetime.datetime.now().strftime("%H:%M:%S")

      # Check whether set alarm is equal to current time or not
      if (curent_time == set_alarm):
         print(" Time to wake up ")
         # Play the sound
         winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
    
# Add label, Frame, Button, Option menues
Label(window, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(window, text="Set Time", font=("Helvetica 20 bold")).pack()

frame = Frame()
frame.pack()

hour = StringVar(window)
hours = (
    '00', '01', '02', '03', '04', '05', '06', '07',
    '08', '09', '10', '11', '12', '13', '14', '15',
    '16', '17', '18', '19', '20', '21', '22', '23'
)
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(window)
minutes = (
    '00', '01', '02', '03', '04', '05', '06', '07',
    '08', '09', '10', '11', '12', '13', '14', '15',
    '16', '17', '18', '19', '20', '21', '22', '23',
    '24', '25', '26', '27', '28', '29', '30', '31',
    '32', '33', '34', '35', '36', '37', '38', '39',
    '40', '41', '42', '43', '44', '45', '46', '47',
    '48', '49', '50', '51', '52', '53', '54', '55',
    '56', '57', '58', '59'
)
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(window)
seconds = (
    '00', '01', '02', '03', '04', '05', '06', '07',
    '08', '09', '10', '11', '12', '13', '14', '15',
    '16', '17', '18', '19', '20', '21', '22', '23',
    '24', '25', '26', '27', '28', '29', '30', '31',
    '32', '33', '34', '35', '36', '37', '38', '39',
    '40', '41', '42', '43', '44', '45', '46', '47',
    '48', '49', '50', '51', '52', '53', '54', '55',
    '56', '57', '58', '59'
)
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(window, text="Set Alarm", font=("Helvetica 20 bold"), command=Threading).pack(pady=20)

# Execute Tkinter
window.mainloop()




