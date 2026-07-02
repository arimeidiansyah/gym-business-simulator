def assign_event_id(events):

    for i, event in enumerate(events, start=1):
        event["event_id"] = f"EVT{i:07d}"

    return events