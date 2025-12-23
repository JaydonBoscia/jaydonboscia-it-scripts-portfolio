from collections import Counter
from datetime import datetime
import os

def analyze_log(file_path):
    if not os.path.exists(file_path):
        return "Log file not found."

    errors = []
    warnings = []

    with open(file_path, "r", errors="ignore") as log:
        for line in log:
            if "error" in line.lower():
                errors.append(line.strip())
            elif "warning" in line.lower():
                warnings.append(line.strip())

    report = []
    report.append(f"Log Analysis Report - {datetime.now().isoformat()}")
    report.append(f"File analyzed: {file_path}")
    report.append("")
    report.append(f"Total Errors: {len(errors)}")
    report.append(f"Total Warnings: {len(warnings)}")

    if errors:
        report.append("\nTop Error Messages:")
        for msg, count in Counter(errors).most_common(5):
            report.append(f"{count}x - {msg}")

    if warnings:
        report.append("\nTop Warning Messages:")
        for msg, count in Counter(warnings).most_common(5):
            report.append(f"{count}x - {msg}")

    output_file = f"log_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(output_file, "w") as f:
        f.write("\n".join(report))

    return f"Log analysis complete. Report generated: {output_file}"

if __name__ == "__main__":
    log_file = input("Enter path to log file: ")
    print(analyze_log(log_file))
