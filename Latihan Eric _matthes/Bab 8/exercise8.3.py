def make_shirt(size, text):
    print(f"The shirt is size {size} and says '{text}'.")


make_shirt("M", "Hello")                # positional
make_shirt(text="Hello", size="M")      # keyword