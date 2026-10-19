# System Log Analyzer

A Python command-line application for reading, parsing, filtering, searching, and reporting system log events.

The project processes log files containing timestamps, severity levels, and messages, then generates summaries and filtered reports.

## Features

- Read log entries from a `.log` file
- Parse log lines into structured Python dictionaries
- Normalize severity levels
- Detect invalid log formats
- Count INFO, WARNING, ERROR, and unknown severity events
- Display important WARNING and ERROR events
- Filter events by severity
- Search log messages by keyword
- Handle missing and empty log files
- Export analysis results to a text report
- Modular project architecture

## Supported Log Format

Each log entry should follow this structure:

```text
YYYY-MM-DD HH:MM:SS SEVERITY Message
```
