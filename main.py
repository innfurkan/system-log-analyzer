import analyzer
import file_handler
import report     

def main():

    log_line_status = {
            "INFO" : "NORMAL",
            "WARNING" : "CHECK SYSTEM",
            "ERROR" : "ATTENTION REQUIRED"
        }

    severity_counts = {
            "INFO":0,
            "WARNING":0,
            "ERROR":0
        }

    log_lines = file_handler.read_log_lines("system.log")

    if log_lines is None:
        print("Unable to analyze logs.")
        return
    elif not log_lines:
        print("There isn't any log line to analyze")
        return

    unknown_severity_count = 0
    parsed_events = []
    invalid_events = []
    important_events = []

    invalid_events, important_events, parsed_events, severity_counts, unknown_severity_count = analyzer.categorize_events(log_lines, invalid_events, important_events, parsed_events, severity_counts,unknown_severity_count)

    report.print_system_log_analyzer(log_lines, log_line_status)

    

    report.print_events(important_events, "IMPORTANT EVENTS")

    invalid_count = len(invalid_events)


    report.print_summary(len(log_lines), invalid_count, severity_counts, unknown_severity_count)

    report.write_summary_report("analysis_report.txt", len(log_lines), invalid_count, severity_counts, unknown_severity_count)


    error_events = analyzer.filter_events_by_severity(parsed_events, "ERROR")
    report.print_events(error_events, "ERROR EVENTS")

    report.append_events_report("analysis_report.txt", error_events, "ERROR")


    sensor_events = analyzer.search_events(parsed_events, "sensor")
    report.print_events(sensor_events, "SENSOR EVENTS")

    report.append_events_report("analysis_report.txt", sensor_events, "SENSOR")


    battery_events = analyzer.search_events(parsed_events, "battery")
    report.print_events(battery_events, "BATTERY EVENTS")

    report.append_events_report("analysis_report.txt", battery_events, "BATTERY") 

    print()


if __name__ == "__main__":
    main()