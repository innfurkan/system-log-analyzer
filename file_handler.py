def read_log_lines(file_name):
    log_lines = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    log_lines.append(clean_line)
        if len(log_lines) == 0:
            print("File founded but it is empty")
        return log_lines
    except FileNotFoundError:
        print("File couldn't be found")
        return None