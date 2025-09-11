import datetime

def greet(name):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello, {name}! Welcome to the sample python module.")
    print(f"The current date and time is: {current_time}")

if __name__ == "__main__":
    user_name = ">>username<<"
    greet(user_name)