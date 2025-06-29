import datetime
import pytz
import sys
import re
import argparse
from kollavarsham import Kollavarsham

def main():
    parser = argparse.ArgumentParser(description="Convert Gregorian dates to Kollavarsham dates.")
    parser.add_argument("date_input", nargs="*", default=None, # Changed nargs to '*'
                        help="Date in dd/mm/yyyy or \"dd/mm/yyyy hh:mm\" format, or 'now'. Defaults to current date at midnight.")
    parser.add_argument("-H", "--human-readable", action="store_true",
                        help="Output in a human-readable format.")

    args = parser.parse_args()

    # Initialize Kollavarsham with required arguments
    # Using approximate coordinates for Kerala, India and a default system
    kv = Kollavarsham(latitude=10.8505, longitude=76.2711, system="SuryaSiddhanta")

    # Determine the Gregorian date
    gregorian_date_obj = None
    
    # Join the date_input arguments if there are multiple parts
    if args.date_input:
        input_str = " ".join(args.date_input).strip('"')
    else:
        input_str = None

    if input_str is None:
        # Default to current date at midnight UTC
        today = datetime.date.today()
        gregorian_date_obj = pytz.utc.localize(datetime.datetime(today.year, today.month, today.day, 0, 0, 0))
    elif input_str.lower() == "now":
        # Use current date and time in UTC
        gregorian_date_obj = datetime.datetime.now(datetime.timezone.utc)
    else:
        # Parse date from dd/mm/yyyy or dd/mm/yyyy hh:mm string
        match = re.match(r"^(\d{2})/(\d{2})/(\d{4})(?:\s+(\d{2}):(\d{2}))?$", input_str)
        if match:
            day, month, year = map(int, match.groups()[0:3])
            hour = int(match.groups()[3]) if match.groups()[3] is not None else 0
            minute = int(match.groups()[4]) if match.groups()[4] is not None else 0
            try:
                gregorian_date_obj = pytz.utc.localize(datetime.datetime(year, month, day, hour, minute, 0))
            except ValueError:
                print("Error: Invalid date or time components.")
                sys.exit(1)
        else:
            print("Error: Invalid date format. Please use dd/mm/yyyy or \"dd/mm/yyyy hh:mm\" or 'now'.")
            sys.exit(1)

    # Convert Gregorian date to Kollavarsham
    kollavarsham_date = kv.from_gregorian_date(date=gregorian_date_obj)

    if args.human_readable:
        print(f"Gregorian {gregorian_date_obj.year}-{gregorian_date_obj.month}-{gregorian_date_obj.day} {gregorian_date_obj.hour:02d}:{gregorian_date_obj.minute:02d} is Kollavarsham: {kollavarsham_date.year} {kollavarsham_date.ml_masa_name} {kollavarsham_date.date} ({kollavarsham_date.ml_naksatra_name})")
    else:
        # Machine-readable output: year,masa_name,date,naksatra_name
        print(f"{kollavarsham_date.year},{kollavarsham_date.ml_masa_name},{kollavarsham_date.date},{kollavarsham_date.ml_naksatra_name}")

if __name__ == "__main__":
    main()