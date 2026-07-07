# Simple Log Parser Script
# This script reads a log file and prints lines containing suspicious keywords.

keywords = ["failed", "error", "unauthorized", "denied"]

def parse_logs(file_path):
    try:
        with open(file_path, "r") as f:
            for line in f:
                if any(keyword in line.lower() for keyword in keywords):
                    print(line.strip())
    except FileNotFoundError:
        print("Log file not found.")

# Example usage:
# parse_logs("auth.log")
