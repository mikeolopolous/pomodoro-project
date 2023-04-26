import tkinter as tk

LIGHT = "#F6F1F1"
LIGHT_BLUE = "#19A7CE"
DARK_BLUE = "#146C94"
BLACK = "#000000"
MINT = "#27E1C1"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓✓✓"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("The Pomodoro Technique 💙")
window.config(padx=20, pady=20, bg=LIGHT)

canvas = tk.Canvas(width=200, height=200, bg=LIGHT, highlightthickness=0)
nerd_img = tk.PhotoImage(file="nerd.png")
canvas.create_image(105, 100, image=nerd_img)
canvas.create_text(100, 107, text="00:00", font=(FONT_NAME, 35, "bold"), fill=LIGHT_BLUE)
canvas.grid(column=1, row=1)

timer_label = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=DARK_BLUE, bg=LIGHT)
timer_label.grid(column=1, row=0, pady=(0, 20))

start_button = tk.Button(text="Start", font=(FONT_NAME, 20))
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 20))
reset_button.grid(column=2, row=2)

checkmark_label = tk.Label(text=CHECKMARK, font=(FONT_NAME, 34, "bold"), fg=MINT, bg=LIGHT)
checkmark_label.grid(column=1, row=3)

window.mainloop()