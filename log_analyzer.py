import re


def analyze_log(file_path):
    results = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0
    }

    error_messages = []
    total_lines = 0
    invalid_lines = 0

    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                total_lines += 1

                match = re.search(
                    r"\[(INFO|WARNING|ERROR|CRITICAL)\]",
                    line
                )

                if match:
                    level = match.group(1)
                    results[level] += 1

                    if level in ("ERROR", "CRITICAL"):
                        message = line.split("] ", 1)[-1].strip()
                        error_messages.append(message)
                else:
                    invalid_lines += 1

        return results, error_messages, total_lines, invalid_lines

    except FileNotFoundError:
        print("Error: Log file not found.")
        return None, [], 0, 0

    except OSError as error:
        print(f"Error reading log file: {error}")
        return None, [], 0, 0