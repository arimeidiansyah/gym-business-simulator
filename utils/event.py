def create_event(
    event_date,
    customer_id,
    event_type,
    product_id=None,
    payment_method=None,
    check_in=None,
    check_out=None,
    duration_minutes=None,
    notes=None
):

    return {
        "event_id": None,
        "event_date": event_date,
        "customer_id": customer_id,
        "event_type": event_type,
        "product_id": product_id,
        "payment_method": payment_method,
        "check_in": check_in,
        "check_out": check_out,
        "duration_minutes":duration_minutes,
        "notes": notes
    }