UPPER_LIMITS = {
    "minute": 60,
    "hour": 24,
    "day of month": 32,
    "month": 13,
    "day of week": 8
}


def validate_range(field_name, start, end):
    upper_limit = UPPER_LIMITS[field_name]
    if start < 1 or end > upper_limit - 1 or end < start:
        raise ValueError(f"Invalid range in {field_name}: {start}-{end}")


def validate_value(field_name, value):
    upper_limit = UPPER_LIMITS[field_name]
    if value < 0 or value >= upper_limit:
        raise ValueError(f"Invalid value in {field_name}: {value}")


def parse_range_segment(field_name, segment):
    start, end = map(int, segment.split("-"))
    validate_range(field_name, start, end)
    return list(range(start, end + 1))


def parse_step_segment(upper_limit, step):
    return list(range(0, upper_limit, step))


def parse_field_segment(field_name, segment):
    value = int(segment)
    validate_value(field_name, value)
    return [value]


def parse_field(field, field_name):
    upper_limit = UPPER_LIMITS[field_name]
    if field == "*":
        start_value = 0 if field_name in ["minute", "hour"] else 1
        return list(range(start_value, upper_limit))

    values = []
    segments = field.split(",")

    for segment in segments:
        if "-" in segment:
            values.extend(parse_range_segment(field_name, segment))
        elif "/" in segment:
            step = int(segment.split("/")[1])
            values.extend(parse_step_segment(upper_limit, step))
        else:
            values.extend(parse_field_segment(field_name, segment))

    return sorted(values)


def validate_cron_expression(expression):
    fields = expression.split(" ")
    if len(fields) != 6:
        raise ValueError("Invalid number of fields in cron expression")
