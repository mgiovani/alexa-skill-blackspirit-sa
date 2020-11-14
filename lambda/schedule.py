from boss import Boss, BossTime


sunday_schedule = {
    BossTime("00:15"): [],
    BossTime("02:00"): [Boss.NOUVER],
    BossTime("11:00"): [Boss.NOUVER, Boss.KARANDA],
    BossTime("16:00"): [Boss.KZARKA, Boss.KARANDA],
    BossTime("18:00"): [Boss.VELL],
    BossTime("20:00"): [Boss.NOUVER, Boss.KARANDA],
    BossTime("23:30"): [Boss.OFFIN]
}
monday_schedule = {
    BossTime("00:15"): [],
    BossTime("02:00"): [Boss.KARANDA, Boss.KZARKA],
    BossTime("11:00"): [Boss.NOUVER],
    BossTime("16:00"): [Boss.KUTUM, Boss.KZARKA],
    BossTime("18:00"): [],
    BossTime("20:00"): [Boss.NOUVER, Boss.KUTUM],
    BossTime("23:30"): [Boss.GARMOTH]
}
tuesday_schedule = {
    BossTime("00:15"): [],
    BossTime("02:00"): [Boss.KUTUM],
    BossTime("11:00"): [Boss.KZARKA],
    BossTime("16:00"): [Boss.NOUVER, Boss.KUTUM],
    BossTime("18:00"): [],
    BossTime("20:00"): [Boss.KZARKA, Boss.KARANDA],
    BossTime("23:30"): [Boss.OFFIN]
}
wednesday_schedule = {
    BossTime("00:15"): [],
    BossTime("02:00"): [Boss.KZARKA],
    BossTime("11:00"): [Boss.KUTUM, Boss.KARANDA],
    BossTime("16:00"): [Boss.KZARKA, Boss.NOUVER],
    BossTime("18:00"): [],
    BossTime("20:00"): [Boss.QUINT_MURAKA],
    BossTime("23:30"): [Boss.GARMOTH]
}
thursday_schedule = {
    BossTime("00:15"): [],
    BossTime("02:00"): [Boss.KARANDA, Boss.KUTUM],
    BossTime("11:00"): [Boss.NOUVER, Boss.KARANDA],
    BossTime("16:00"): [Boss.KUTUM, Boss.KZARKA],
    BossTime("18:00"): [],
    BossTime("20:00"): [Boss.NOUVER, Boss.KUTUM],
    BossTime("23:30"): []
}
friday_schedule = {
    BossTime("00:15"): [Boss.VELL],
    BossTime("02:00"): [Boss.KARANDA, Boss.OFFIN],
    BossTime("11:00"): [Boss.NOUVER],
    BossTime("16:00"): [Boss.KUTUM, Boss.KZARKA],
    BossTime("18:00"): [],
    BossTime("20:00"): [Boss.NOUVER, Boss.KZARKA],
    BossTime("23:30"): [Boss.GARMOTH]
}
saturday_schedule = {
    BossTime("00:15"): [],
    BossTime("02:00"): [Boss.KZARKA],
    BossTime("11:00"): [Boss.KZARKA, Boss.KARANDA],
    BossTime("16:00"): [Boss.NOUVER, Boss.KUTUM],
    BossTime("18:00"): [],
    BossTime("20:00"): [Boss.QUINT_MURAKA],
    BossTime("23:30"): []
}
week_schedule = [sunday_schedule, monday_schedule, tuesday_schedule, wednesday_schedule, thursday_schedule, friday_schedule, saturday_schedule]
