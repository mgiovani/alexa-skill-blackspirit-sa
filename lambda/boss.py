from datetime import datetime
from enum import Enum


class BossTime():
    def __init__(self, str_time):
        self.str_time = str_time
        self.time = datetime.strptime(str_time, "%H:%M").time()

    def __str__(self):
        return self.str_time

    def __repr__(self):
        return self.str_time


class BossClass():
    def __init__(self, boss_name):
        self.boss_name = boss_name

    def __str__(self):
        return self.boss_name

    def __repr__(self):
        return self.boss_name


class Boss(Enum):
    GARMOTH = BossClass("Garmoth")
    KARANDA = BossClass("Karanda")
    KUTUM = BossClass("Kutum")
    KZARKA = BossClass("Kzarka")
    NOUVER = BossClass("Nouver")
    OFFIN = BossClass("Offin")
    QUINT_MURAKA = BossClass("Quint_Muraka")
    VELL = BossClass("Vell")

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)
