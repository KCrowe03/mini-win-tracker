from datetime import date
import csv
import os

# Step 1: Get today's date
today = date.today()

# Step 2: Ask your mini-win question
print(f"\nMini-Win Tracker – {today}")
win = input("What is one thing you did today that you're proud of?\n> ")

# Step 3: Create or append to the CSV file
filename = "mini_win_log.csv"
file_exists = os.path.isfile(filename)

# Step 4: Open the file and write the entry
with open(filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["Date", "Mini Win"])  # header
    writer.writerow([today, win])

# Step 5: Confirm to the user
print("\n✅ Win logged! You're doing great.")

