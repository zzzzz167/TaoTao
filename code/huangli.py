# _*_ coding:utf-8_*_
import datetime
from lunar_python import Lunar,Solar
def get():
    calendars = Solar.fromDate(datetime.datetime.now())
    calendars_str = calendars.toFullString()
    calendars_Festivals = ','.join(calendars.getFestivals()) + ','.join(calendars.getOtherFestivals())

    lunarcakendar = Lunar.fromDate(datetime.datetime.now())
    lunarcalendar_year = lunarcakendar.getYearInChinese()
    lunarcalendar_month = lunarcakendar.getMonthInChinese()
    lunarcalendar_day = lunarcakendar.getDayInChinese()
    lunarcakendar_appropriate = ','.join(lunarcakendar.getDayYi())
    lunarcakendar_avoid = ','.join(lunarcakendar.getDayJi())
    lunarcakendar_Festivals = ','.join(lunarcakendar.getFestivals()) + ','.join(lunarcakendar.getOtherFestivals())
    prev = lunarcakendar.getPrevJieQi()
    prev_JieQi = prev.getName()
    next = lunarcakendar.getNextJieQi()
    next_JieQi = "{} {}".format(next.getName(), next.getSolar().toYmdHms())
    PengZu = lunarcakendar.getPengZuGan() + ',' + lunarcakendar.getPengZuZhi()
    CaiShen = lunarcakendar.getDayPositionCai() + '-' + lunarcakendar.getDayPositionCaiDesc()
    FuShen = lunarcakendar.getDayPositionFu() + '-' + lunarcakendar.getDayPositionFuDesc()
    XiShen = lunarcakendar.getDayPositionXi() + '-' + lunarcakendar.getDayPositionXiDesc()
    YuXiang = lunarcakendar.getYueXiang()
    WuHou = lunarcakendar.getWuHou()

    res = "今天是：\n" \
          "公元>{}\n" \
          "阴历>{} {}月 {}\n" \
          "宜>{}\n" \
          "忌>{}\n" \
          "上一节气>{}\n" \
          "下一节气>{}\n" \
          "传统节日>{}\n" \
          "法定节日>{}\n" \
          "彭祖百忌>{}\n" \
          "财福喜神>财神:{},福神:{},喜神：{}\n" \
          "月相>{}\n" \
          "今日物候>{}".format(
        calendars_str,
        lunarcalendar_year, lunarcalendar_month, lunarcalendar_day,
        lunarcakendar_appropriate,
        lunarcakendar_avoid,
        prev_JieQi,
        next_JieQi,
        lunarcakendar_Festivals,
        calendars_Festivals,
        PengZu,
        CaiShen, FuShen, XiShen,
        YuXiang,
        WuHou
    )
    return res