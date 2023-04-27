import tkinter as tk
import math

LIGHT = "#F6F1F1"
LIGHT_BLUE = "#19A7CE"
DARK_BLUE = "#146C94"
BLACK = "#000000"
MINT = "#27E1C1"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", fill=BLACK)
    timer_label.config(text="Timer", fg=BLACK)
    checkmark_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0: 
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=DARK_BLUE)
        canvas.itemconfig(timer_text, fill=DARK_BLUE)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=LIGHT_BLUE)
        canvas.itemconfig(timer_text, fill=LIGHT_BLUE)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=MINT)
        canvas.itemconfig(timer_text, fill=MINT)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✓"
        
        checkmark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("The Pomodoro Technique 💙")
window.config(padx=20, pady=20, bg=LIGHT)

canvas = tk.Canvas(width=200, height=200, bg=LIGHT, highlightthickness=0)
nerd_img = tk.PhotoImage(file="nerd.png")
canvas.create_image(105, 100, image=nerd_img)
timer_text = canvas.create_text(100, 107, text="00:00", font=(FONT_NAME, 35, "bold"), fill=BLACK)
canvas.grid(column=1, row=1)

timer_label = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=BLACK, bg=LIGHT)
timer_label.grid(column=1, row=0, pady=(0, 20))

start_button = tk.Button(text="Start", font=(FONT_NAME, 20), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 20), command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = tk.Label(font=(FONT_NAME, 34, "bold"), fg=MINT, bg=LIGHT)
checkmark_label.grid(column=1, row=3)

window.mainloop()