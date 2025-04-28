import time

def countdown(x):
    while x:
        mins, sec = divmod(x, 60)
        timer = f"{mins:02d}:{sec:02d}"
        print(timer, end="\r")
        time.sleep(1)
        x -= 1
    print("Time's up!")

def main():
    try:
        sec = int(input("Enter time in seconds: "))
        countdown(sec)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
