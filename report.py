import analyzer

def print_events(events, title):
    print()
    print(f"{title}")
    print("-" * len(title))
    if events == None:
        return None
    elif events == []:
        print("NO EVENT FOUND")
        return
    for event in events:
        print(f"{event["time"]} {event["severity"]} - {event["message"]}")

def print_summary(total_lines, invalid_lines, severity_counts, unknown_severity_counts):
    print()
    print("SUMMARY")
    print("-------")
    print(f"Total Lines: {total_lines}")
    print(f"Valid Events: {total_lines - invalid_lines}")
    print(f"Invalid Events: {invalid_lines}")
    print()
    print(f"INFO: {severity_counts["INFO"]}")
    print(f"WARNING: {severity_counts["WARNING"]}")
    print(f"ERROR: {severity_counts["ERROR"]}")
    print(f"UNKNOWN SEVERITY: {unknown_severity_counts}")

def print_system_log_analyzer(log_lines, log_line_status):
    print()
    print("SYSTEM LOG ANALYZER")
    print("-------------------")
    
    i=0
    for log_line in log_lines:
        i += 1
        if analyzer.is_appropriate_format(log_line):
            date, time, severity, message = analyzer.get_log_line_in_string(log_line)
            print(f"Log Line {i}")
            print(f"Date: {date}")
            print(f"Time: {time}")
            print(f"Severity: {severity}")
            print(f"Message: {message}")
            if severity in log_line_status:
                print(f"Status: {log_line_status[severity]}")
            else:
                print(f"UNDEFINE STATUS: {severity}")
            print()   
        else:
            print(f"Log Line {i} is not in appropriate format")

def write_summary_report(file_name, total_lines, invalid_lines, severity_counts, unknown_severity_counts):
    with open(file_name, "w") as file:
        file.write("SUMMARY\n")
        file.write("-------\n")
        file.write(f"Total Events: {total_lines}\n")
        file.write(f"Valid Events: {total_lines - invalid_lines}\n")
        file.write(f"Invalid Events: {invalid_lines}\n")
        file.write("\n")
        file.write(f"INFO: {severity_counts["INFO"]}\n")
        file.write(f"WARNING: {severity_counts["WARNING"]}\n")
        file.write(f"ERROR: {severity_counts["ERROR"]}\n")
        file.write(f"UNKNOWN SEVERITY: {unknown_severity_counts}\n")
        print()
        print("Summary Report saved to analysis_report.txt")
        print()
        print("-------------------------------------------")

def append_events_report(file_name, events, title):
    with open(file_name, "a") as file:
        file.write("\n")
        file.write(f"{title} EVENTS\n")
        file.write("-" * len(title))
        file.write("\n")
        if events is None:
            return False
        
        if not events:
            file.write("NO EVENT FOUND\n")

        for event in events:
            file.write(f'{event["time"]} ' f'{event["severity"]} - ' '{event["message"]}\n')
        print()
        print(f"{title} Report saved to analysis_report.txt")
        print()
        print("-------------------------------------------")

