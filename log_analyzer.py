import re


def analyze_log(file_path):
    results = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0
    }

    error_messages = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                match = re.search(r"\[(INFO|WARNING|ERROR|CRITICAL)\]", line)

                if match:
                    level = match.group(1)
                    results[level] += 1

                    if level in ("ERROR", "CRITICAL"):
                        message = line.split("] ", 1)[-1].strip()
                        error_messages.append(message)

        return results, error_messages

    except FileNotFoundError:
        print("Error: Log file not found.")
        return None, []

    except OSError as error:
        print(f"Error reading log file: {error}")
        return None, []