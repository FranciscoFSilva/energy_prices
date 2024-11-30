from datetime import datetime, timedelta


def get_tomorrows_datetime() -> datetime:
    return datetime.today() + timedelta(days=1)


def datetime_as_str(date: datetime) -> str:
    """get_datetime_as_str"""
    return date.strftime("%d_%m_%Y")
