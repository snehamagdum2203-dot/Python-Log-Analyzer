from log_analyzer import analyze_log
from report_generator import generate_report


REPORT_FILE = "report.txt"


def main():
    print("===== PYTHON LOG ANALYZER =====")

    log_file = input("Enter log file path: ").strip()

    if not log_file:
        print("Error: Log file path cannot be empty.")
        return

    print(f"\nAnalyzing: {log_file}\n")

    results, error_messages, total_lines, invalid_lines = analyze_log(log_file)

    if results is None:
        return

    generate_report(
        results,
        error_messages,
        total_lines,
        invalid_lines,
        REPORT_FILE
    )

    print("\nLog analysis completed successfully.")


if __name__ == "__main__":
    main()