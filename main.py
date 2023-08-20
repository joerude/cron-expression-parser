import sys

from utils import validate_cron_expression, parse_field


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <cron_expression>")
        return

    cron_expression = sys.argv[1]
    validate_cron_expression(cron_expression)

    field_names = ["minute", "hour", "day of month", "month", "day of week"]

    for i, field in enumerate(cron_expression.split(" ")[:5]):
        field_values = parse_field(field, field_names[i])
        print(f"{field_names[i]:<14} {' '.join(map(str, field_values))}")

    print(f"command {' '.join(cron_expression.split(' ')[5:])}")


if __name__ == "__main__":
    main()
