import datetime
from video import Video
from tkinter import *
from tkinter import messagebox

BG = "black"
TITLE ="white"
HMS = "#AAD8D3"
INPUT = "#393E46"
FONT_NAME = "Courier"

# ---------------------------- ALARM SETUP ------------------------------- #

def set_the_alarm():
    video = Video()

    def alarm(setting_time):
        alarm_on = True
        while alarm_on:
            #  Display the current time
            current_date = datetime.datetime.now()
            current_time = current_date.strftime("%H:%M:%S")
            # print(current_time)

            #  Comparing current time and setting time
            if current_time == setting_time:
                print("Alarm clock")
                alarm_on = False
                video.utube_video()

    hour = hour_input.get()
    minutes = min_input.get()
    seconds = sec_input.get()

    # Checks whether we have put the timings if not gives warning to put the timings
    if len(hour)==0 or len(minutes)==0 or len(seconds)==0:
        messagebox.showinfo(title="Warning", message="Please enter the timings.")
    else:
        set_alarm = f"{hour}:{minutes}:{seconds}"
        alarm(set_alarm)
        hour_input.delete(0, END)
        min_input.delete(0, END)
        sec_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("ALARM")
# window.minsize(width=200, height=200)
window.config(padx=50, pady=50, bg=BG)
# window.maxsize(width=200, height=200)

#  Label
label = Label(text="24 hours format", fg=TITLE, bg=BG , font=(FONT_NAME, 20, "bold"))
label.grid(row=0, column=0, columnspan=5)

hour_label = Label(text="Hour",fg=HMS, bg=BG, font=(FONT_NAME, 20, "bold"))
hour_label.grid(row=2, column=0)
colon_label = Label(text=":", fg=TITLE, bg=BG, font=(FONT_NAME, 20, "bold"))
colon_label.grid(row=1, column=1)
minute_label = Label(text="Minute", fg=HMS, bg=BG, font=(FONT_NAME, 20, "bold"))
minute_label.grid(row=2, column=2)
colon_label1 = Label(text=":", fg=TITLE, bg=BG, font=(FONT_NAME, 20, "bold"))
colon_label1.grid(row=1, column=3)
second_label = Label(text="Second", fg=HMS, bg=BG, font=(FONT_NAME, 20, "bold"))
second_label.grid(row=2, column=4)

# Enter
hour_input = Entry(width=6, fg=TITLE, bg=INPUT, font=(FONT_NAME, 20, "bold"))
hour_input.grid(row=1, column=0)
min_input = Entry(width=6, fg=TITLE, bg=INPUT, font=(FONT_NAME, 20, "bold"))
min_input.grid(row=1, column=2)
sec_input = Entry(width=6, fg=TITLE, bg=INPUT, font=(FONT_NAME, 20, "bold"))
sec_input.grid(row=1, column=4)

# Button
set_button = Button(text="SET", fg="white", bg=INPUT, font=(FONT_NAME, 20, "bold"), command=set_the_alarm)
set_button.grid(row=3, column=2)

window.mainloop()
