# Read and print the contents of keylog.txt

def print_keylog():
    try:
        with open("keylog.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("The keylog.txt file does not exist. Make sure the keylogger has run and created the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_keylog()
