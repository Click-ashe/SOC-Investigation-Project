# Sample Incident Report

## Incident Summary
Suspicious authentication attempts detected from an unknown IP address. Multiple failed logins observed within a short time window.

## Timeline
- 10:32 AM — First failed login attempt
- 10:33 AM — Additional failed attempts from same IP
- 10:35 AM — Account locked due to repeated failures

## Findings
- Source IP: 192.168.10.55
- Target account: user_admin
- Behavior suggests possible brute-force attempt

## Recommended Actions
- Block source IP
- Reset affected account credentials
- Review authentication logs for related activity
- Notify security team for further investigation
