def parse_log_line(log_line):
    parts = log_line.split(maxsplit=3)
    if len(parts) < 4:
        return None
    return {
        "date": parts[0],
        "time": parts[1],
        "severity": parts[2].upper(),
        "message": parts[3]
    }

def is_appropriate_format(log_line):
    result = parse_log_line(log_line)
    if result is None:
        return False
    return True

def get_log_line_in_string(log_line):
    result = parse_log_line(log_line)
    return result["date"], result["time"], result["severity"], result["message"]

def categorize_events(log_lines, invalid_events, important_events, parsed_events, severity_counts, unknown_severity_count):
    for log_line in log_lines:
        if is_appropriate_format(log_line):
            date, time, severity, message = get_log_line_in_string(log_line)
            if severity in severity_counts:
                severity_counts[severity] +=1
            else:
                unknown_severity_count += 1
            parsed_events.append(parse_log_line(log_line))

            if parse_log_line(log_line)["severity"] in ["WARNING", "ERROR"]:
                important_events.append(parse_log_line(log_line))

            continue
        else:
            invalid_events.append(log_line)

    return invalid_events, important_events, parsed_events, severity_counts, unknown_severity_count

def filter_events_by_severity(events, target_severity):
    filtered_events = []
    target_severity = target_severity.upper()
    for event in events:
        if target_severity == event["severity"]:
            filtered_events.append(event)
    return filtered_events

def search_events(events, keyword):
    matching_events = []
    keyword = keyword.lower()
    for event in events:
        event_message = event["message"].lower()
        if keyword in event_message:
            matching_events.append(event)
    return matching_events