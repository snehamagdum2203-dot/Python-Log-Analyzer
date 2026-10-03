from log_analyzer import analyze_log
from report_generator import generate_report


LOG_FILE = "sample.log"
REPORT_FILE = "report.txt"


def main():
    print("===== PYTHON LOG ANALYZER =====")
    print(f"Analyzing: {LOG_FILE}\n")

    results, error_messages = analyze_log(LOG_FILE)

    if results is None:
        return

    generate_report(results, error_messages, REPORT_FILE)

    print("\nLog analysis completed successfully.")


if __name__ == "__main__":
    main()