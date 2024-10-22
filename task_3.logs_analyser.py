import sys
from typing import List, Dict, Optional

def parse_log_line(line: str) -> Dict:
    parts = line.split(' ', 3)
    if len(parts) != 4:
        return {}
    date, time, level, message = parts
    return {
        'date': date,
        'time': time,
        'level': level,
        'message': message.strip()
    }

def load_logs(file_path: str) -> List[Dict]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError:
        print(f"Error reading file: {file_path}")
    return logs

def filter_logs_by_level(logs: List[Dict], level: str) -> List[Dict]:
    return list(filter(lambda log: log['level'].lower() == level.lower(), logs))

def count_logs_by_level(logs: List[Dict]) -> Dict[str, int]:
    log_counts = {}
    for log in logs:
        level = log['level']
        if level in log_counts:
            log_counts[level] += 1
        else:
            log_counts[level] = 1
    return log_counts

def display_log_counts(counts: Dict[str, int]):
    print("  Log level      |   Count  ")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main(file_path: str, filter_level: Optional[str] = None):
    logs = load_logs(file_path)
    if not logs:
        print("No logs to process.")
        return
    
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)
    
    if filter_level:
        filtered_logs = filter_logs_by_level(logs, filter_level)
        if filtered_logs:
            print(f"\nLogs for '{filter_level.upper()}' level:")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"No logs found for level: {filter_level}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tasl_3.logs_analyser.py path/to/logfile.log [level]")
    else:
        file_path = sys.argv[1]
        level = sys.argv[2] if len(sys.argv) > 2 else None
        main(file_path, level)
