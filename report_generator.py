from datetime import datetime


def generate_report(
    results,
    error_messages,
    total_lines,
    invalid_lines,
    output_file
):
    total_entries = sum(results.values())
    problem_entries = results["ERROR"] + results["CRITICAL"]

    if total_entries > 0:
        error_rate = (problem_entries / total_entries) * 100
    else:
        error_rate = 0

    if results["CRITICAL"] > 0:
        overall_status = "CRITICAL"
    elif results["ERROR"] > 0:
        overall_status = "WARNING"
    else:
        overall_status = "HEALTHY"

    try:
        with open(output_file, "w") as file:
            file.write("===== LOG ANALYSIS REPORT =====\n\n")

            file.write(
                f"Report Generated: "
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            )

            file.write(f"Total Log Lines    : {total_lines}\n")
            file.write(f"Valid Log Entries  : {total_entries}\n")
            file.write(f"Invalid Log Lines  : {invalid_lines}\n\n")

            file.write("Log Level Summary:\n")
            file.write(f"INFO              : {results['INFO']}\n")
            file.write(f"WARNING           : {results['WARNING']}\n")
            file.write(f"ERROR             : {results['ERROR']}\n")
            file.write(f"CRITICAL          : {results['CRITICAL']}\n\n")

            file.write(f"Error Rate        : {error_rate:.2f}%\n")
            file.write(f"Overall Status    : {overall_status}\n\n")

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