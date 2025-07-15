import sys
from croniter import croniter
from datetime import datetime
import argparse
from termcolor import colored


def get_human_readable(cron_exp):
    parts = cron_exp.split()
        if len(parts) != 5:
                return None, "❌ Invalid cron expression (must have 5 fields)."

                    minute, hour, dom, month, dow = parts

                        dow_map = {
                                "0": "Sunday", "1": "Monday", "2": "Tuesday", "3": "Wednesday",
                                        "4": "Thursday", "5": "Friday", "6": "Saturday", "7": "Sunday"
                                            }

                                                try:
                                                        next_run = croniter(cron_exp, datetime.now()).get_next(datetime)
                                                            except:
                                                                    return None, "❌ Unable to parse the cron expression."

                                                                        # Build human description
                                                                            schedule = f"⏰ This job runs at {hour}:{minute} "
                                                                                if dom == "*" and dow != "*":
                                                                                        schedule += f"on every {dow_map.get(dow, dow)}"
                                                                                            elif dom != "*" and dow == "*":
                                                                                                    schedule += f"on day {dom} of every month"
                                                                                                        elif dom == "*" and dow == "*":
                                                                                                                schedule += "every day"
                                                                                                                    else:
                                                                                                                            schedule += f"on day {dom} and {dow_map.get(dow, dow)}"

                                                                                                                                if month != "*":
                                                                                                                                        schedule += f" in month {month}"

                                                                                                                                            schedule += f"\n📆 Next run: {next_run.strftime('%Y-%m-%d %H:%M:%S')}"

                                                                                                                                                return schedule, None


                                                                                                                                                def main():
                                                                                                                                                    parser = argparse.ArgumentParser(description="🧠 Crontab Explainer")
                                                                                                                                                        parser.add_argument("expression", help="Cron expression in quotes (e.g. '0 2 * * 1')")
                                                                                                                                                            args = parser.parse_args()

                                                                                                                                                                result, error = get_human_readable(args.expression)

                                                                                                                                                                    if error:
                                                                                                                                                                            print(colored(error, "red"))
                                                                                                                                                                                else:
                                                                                                                                                                                        print(colored("✅ Cron Expression Breakdown:", "green"))
                                                                                                                                                                                                print(result)


                                                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                                                    main()
                                                                                                                                                                                                    