from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    # day = date(2023, 12, 28)
    day = date.today()
    dic_birthdays_per_week = {"Monday": [], "Tuesday": [], "Wednesday": [],
                              "Thursday": [], "Friday": []}
    DIC_WEEK_DAY = {1: "Monday", 2: "Tuesday", 3: "Wednesday",
                    4: "Thursday", 5: "Friday", 6: "Monday", 7: "Monday"}

    for dic in users:
        variable = (day + timedelta(weeks=1)).day
        dic_month = dic["birthday"].month
        dic_day = dic["birthday"].day

        if dic_month - day.month in [-11, 1] and 0 < dic_day < variable:
            True_False = True
        elif dic_month == day.month and 0 <= dic_day - day.day <= 7:
            True_False = True
        else:
            True_False = False

        if True_False:
            key = dic["birthday"]

            if key.month - day.month == -11:
                key = key.replace(year=day.year + 1)
            else:
                key = key.replace(year=day.year)

            key = DIC_WEEK_DAY[key.isoweekday()]

            if key in dic_birthdays_per_week:
                dic_birthdays_per_week[key] += [dic["name"]]
            else:
                dic_birthdays_per_week[key] = [dic["name"]]
    for num in range(1, 6):
        key = DIC_WEEK_DAY[num]

        if not dic_birthdays_per_week[key]:
            dic_birthdays_per_week.pop(key)
    return dic_birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "1", "birthday": datetime(1950, 1, 2).date()},
        {"name": "2", "birthday": datetime(2023, 12, 29).date()},
        {"name": "3", "birthday": datetime(1950, 1, 3).date()},
        {"name": "4", "birthday": datetime(2023, 11, 15).date()},
        {"name": "5", "birthday": datetime(1950, 12, 30).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
