def sort(emails):
    # sort by domain (after @), then by username (before @)
    # use .lower() for case-insensitive comparison
    sorted_emails = sorted(emails, key=lambda email: email.lower().split('@')[::-1])
    return sorted_emails

print(sort(["jill@mail.com", "john@example.com", "jane@example.com"]))