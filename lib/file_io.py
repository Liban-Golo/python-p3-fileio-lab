

def write_file(file_name, file_content):
    """Writes content to a .txt file, overwriting if it exists."""
    with open(f"{file_name}.txt", "w") as f:
        f.write(file_content) 


def append_file(file_name, append_content):
    """Appends content to a .txt file."""
    with open(f"{file_name}.txt", "a") as f:
        f.write(append_content)  


def read_file(file_name):
    """Reads the content of a .txt file and returns it as a string."""
    with open(f"{file_name}.txt", "r") as f:
        return f.read()
