from global_filter_github import filter_include_event


def rule(event):
    if not filter_include_event(event):
        return False
    return event.get("action") == "secret_scanning_alert.create"


def title(event):
    return f"Github detected a secret in {event.get('repo')} (#{event.get('number')})"


def alert_context(event):
    return {
        "repo": event.get("repo"),
        "alert #": event.get("number"),
        "url": f"https://github.com/{event.get('repo')}/security/secret-scanning/"
        f"{event.get('number')}",
    }
