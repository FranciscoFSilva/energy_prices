from datetime import datetime, timedelta


def get_tomorrows_datetime() -> datetime:
    return datetime.today() + timedelta(days=1)


def datetime_as_str(date: datetime) -> str:
    """get_datetime_as_str"""
    return date.strftime("%Y%m%d")


def get_tomorrow_date_as_str() -> str:
    return datetime_as_str(get_tomorrows_datetime())
