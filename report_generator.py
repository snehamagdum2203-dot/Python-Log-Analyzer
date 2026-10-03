from datetime import datetime


def generate_report(results, error_messages, output_file):
    total_entries = sum(results.values())

    try:
        with open(output_file, "w") as file:
            file.write("===== LOG ANALYSIS REPORT =====\n\n")
            file.write(
                f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            )

            file.write(f"Total Log Entries : {total_entries}\n\n")

            file.write("Log Level Summary:\n")
            file.write(f"INFO              : {results['INFO']}\n")
            file.write(f"WARNING           : {results['WARNING']}\n")
            file.write(f"ERROR             : {results['ERROR']}\n")
            file.write(f"CRITICAL          : {results['CRITICAL']}\n\n")

            file.write("Error and Critical Messages:\n")

            if error_messages:
                for message in error_messages:
                    file.write(f"- {message}\n")
            else:
                file.write("No errors or critical issues found.\n")

            file.write("\n===== END OF REPORT =====\n")

        print(f"Report generated successfully: {output_file}")

    except OSError as error:
        print(f"Error generating report: {error}")