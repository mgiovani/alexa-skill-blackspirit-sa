import logging
import os
from calendar import Calendar
from datetime import datetime, timedelta


from boss import Boss
from schedule import week_schedule


def find_next_boss_today():
    now = datetime.utcnow() - timedelta(seconds=10800)  # -3 hours
    today_schedule = week_schedule[now.isoweekday()]
    for time, boss_list in today_schedule.items():
        if time.time > now.time() and boss_list:
            return (boss_list, time)
    return ()


def find_first_boss_tomorrow():
    now = datetime.utcnow() - timedelta(seconds=10800)  # -3 hours
    tomorrow_schedule = week_schedule[now.isoweekday()+1]
    for time, boss_list in tomorrow_schedule.items():
        if boss_list:
            return (boss_list, time)
    return ()


def find_next_boss():
    boss_list, boss_time = find_next_boss_today()
    if not boss_list:
        boss_list, boss_time = find_first_boss_tomorrow()
    return boss_list, boss_time if boss_list else ()


def find_next_boss_by_name(boss_name):
    boss = Boss[boss_name.upper()]
    now = datetime.utcnow() - timedelta(seconds=10800)  # -3 hours
    day = now.isoweekday()
    day_generator = Calendar(firstweekday=day).iterweekdays()

    schedule = week_schedule[day]
    for time, boss_list in schedule.items():
        if time.time > now.time() and boss in boss_list:
            return (boss_name, time, "hoje")
    next(day_generator)

    for week_day in day_generator:
        schedule = week_schedule[week_day]
        for time, boss_list in schedule.items():
            if boss in boss_list:
                return (boss_list, time, get_weekday_name(week_day))
    return ()


def get_weekday_name(day):
    week_day_name = {
        0: "domingo",
        1: "segunda",
        2: "terça",
        3: "quarta",
        4: "quinta",
        5: "sexta",
        6: "sábado",
    }
    return week_day_name[day]
