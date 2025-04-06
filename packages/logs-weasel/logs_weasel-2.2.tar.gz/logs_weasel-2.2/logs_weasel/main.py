from enum import Enum
from unittest.mock import patch
import redis
import datetime
import traceback
import requests
import warnings


class LogsWeasel:

    class _TypesErrors(Enum):
        info = 'INFO'
        info_start = 'INFO - START'
        info_done = 'INFO - DONE'
        info_not_done = 'INFO - NOT DONE'
        warning = 'WARNING'
        warning_not_done = 'WARNING - NOT DONE'
        warning_error = 'WARNING - ERROR'
        critical = 'CRITICAL'
        critical_fatal = 'CRITICAL - FATAL!'

    class _IconsErrors(Enum):
        info = '✅'
        info_start = '✅'
        info_done = '✅'
        info_not_done = '✅'
        warning = '⚠️'
        warning_not_done = '⚠️'
        warning_error = '⚠️'
        critical = '‼️'
        critical_fatal = '‼️'

    class _ColorCodesErrors(Enum):
        info = 92
        info_start = 92
        info_done = 92
        info_not_done = 92
        warning = 93
        warning_not_done = 93
        warning_error = 93
        critical = 91
        critical_fatal = 91

    _DEFAULT_SETTINGS = {
        'redis_connection': {
            'host': 'localhost',
            'port': 6379,
            'username': 'default',
            'password': None,
            'db': 0
        },
        'redis_files': {
            'frequency': 'day',
            'prefix_file': 'log_'
        },
        'telegram_token': None,
        'users_list': None
    }

    def __init__(self, settings: dict):
        """
Information records/notifications. Marked in green in the terminal
    log.info() - default message

    log.info_start.value() - usually used when starting a function

    log.info_done.value() - usually used when a function has completed successfully

    log.info_not_done.value() - used when a function has not completed

Notices to watch out for. Marked in yellow in the terminal.
    log.warning() - important low

    log.warning_not_done() - important medium

    log.warning_error() - important high

Critical notices. They have the ability to save in the terminal full descriptions of the errors that have occurred.
    log.critical() - error with important high

    log.critical_fatal() - error with important very high, х_х

settings (dict):
    {'redis_connection': {
        'db': {{id_database, default that 0, int}},

        'host': {{redis_host, str}}),

        'port': {{number_of_port, int}},

        'username': {{username, str}},

        'password': {{password, str}},
    'redis_files': {
        'prefix_file': 'logs_',

        'frequency': {{'day'/'week'/'month'}}},

        'telegram_token': {{you_tg_token, str}},

        'users_list': [{{telegram id, int ...}}]
        """
        self._SETTINGS = {**self._DEFAULT_SETTINGS, **settings,
                         'redis_connection': {**self._DEFAULT_SETTINGS['redis_connection'],
                                              **settings.get('redis_connection', {})},
                         'redis_files': {**self._DEFAULT_SETTINGS['redis_files'], **settings.get('redis_files', {})}}
        self._TYPES_ERR = self._TypesErrors
        self._ICONS_ERR = self._IconsErrors
        self._COLOR_CODES_ERR = self._ColorCodesErrors

    def _redis_init(self) -> redis.Redis | bool | None:
        redis_conn = self._SETTINGS.get('redis_connection')
        if not redis_conn:
            return None
        try:
            r = redis.Redis(
                host=redis_conn['host'],
                port=redis_conn['port'],
                username=redis_conn['username'],
                password=redis_conn['password'],
                db=redis_conn['db'],
                decode_responses=True,
                socket_connect_timeout=2,
                ssl_cert_reqs=None,
                ssl=False,
            )
        except Exception:
            traceback.print_exc()
            return False
        return r

    def _dt_now(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _generate_week(self) -> str:
        weekday = datetime.date.today().weekday()
        end_timedelta = 6 - weekday
        start_weekday = datetime.date.today() - datetime.timedelta(days=weekday)
        end_weekday = datetime.date.today() + datetime.timedelta(days=end_timedelta)
        week_str = f'{start_weekday.strftime("%Y-%m-%d")}_{end_weekday.strftime("%Y-%m-%d")}'
        return week_str

    def _add_log_to_redis(self, message: str, postfix: str) -> None:
        if self._SETTINGS['redis_connection'] is None:
            warnings.warn("Redis connection is not set!", category=UserWarning)
            return
        else:
            try:
                r = self._redis_init()
                if r is False or r is None:
                    return
                else:
                    if self._SETTINGS['redis_files']['frequency'] == 'day':
                        r.append(self._SETTINGS['redis_files']['prefix_file'] + str(datetime.date.today()) + postfix, f'\n{message}')
                    elif self._SETTINGS['redis_files']['frequency'] == 'month':
                        r.append(self._SETTINGS['redis_files']['prefix_file'] + datetime.date.today().strftime('%Y-%m') + postfix, f'\n{message}')
                    elif self._SETTINGS['redis_files']['frequency'] == 'week':
                        r.append(self._SETTINGS['redis_files']['prefix_file'] + self._generate_week() + postfix, f'\n{message}')
                    else:
                        raise Exception('Bad SETTINGS["redis_files"]["frequency"]')
            except Exception:
                traceback.print_exc()

    def _send_message(self, message: str) -> None:
        telegram_token = self._SETTINGS.get('telegram_token')
        users_list = self._SETTINGS.get('users_list')
        if not telegram_token or not users_list:
            warnings.warn("telegram_token or users_list is not set!", category=UserWarning)
            return
        else:
            url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
            for user_id in users_list:
                try:
                    payload = {
                        'chat_id': user_id,
                        'text': message
                    }
                    response = requests.post(url, data=payload)
                    if response.status_code != 200:
                        print(f"Failed to send message to {user_id}: {response.text}")
                except Exception:
                    traceback.print_exc()

    def _execute_error(self, type_error, icon_error,
                      color_code, message, postfix, send, exc):
        traceback_row = f'\n{traceback.format_exc()}' if exc else ''
        message_full = f'{type_error} || {self._dt_now()} || {message}{traceback_row}'
        print(f'\033[{color_code}m{message_full}\033[0m')
        self._add_log_to_redis(message_full, postfix)
        self._send_message(f'{icon_error} {type_error}\n_ _ _ _ _\n{message}') if send is True else None

    def info(self, message: str, postfix: str = '', send: bool = False, exc: bool = False) -> None:
        self._execute_error(self._TYPES_ERR.info.value,
                           self._ICONS_ERR.info.value,
                           self._COLOR_CODES_ERR.info.value,
                           message, postfix, send, exc)

    def info_start(self, message: str, postfix: str = '', send: bool = False, exc: bool = False) -> None:
        self._execute_error(self._TYPES_ERR.info_start.value,
                           self._ICONS_ERR.info_start.value,
                           self._COLOR_CODES_ERR.info_start.value,
                           message, postfix, send, exc)

    def info_done(self, message: str, postfix: str = '', send: bool = False, exc: bool = False) -> None:
        self._execute_error(self._TYPES_ERR.info_done.value,
                           self._ICONS_ERR.info_done.value,
                           self._COLOR_CODES_ERR.info_done.value,
                           message, postfix, send, exc)

    def info_not_done(self, message: str, postfix: str = '', send: bool = False, exc: bool = False) -> None:
        self._execute_error(self._TYPES_ERR.info_not_done.value,
                           self._ICONS_ERR.info_not_done.value,
                           self._COLOR_CODES_ERR.info_not_done.value,
                           message, postfix, send, exc)

    def warning(self, message: str, postfix: str = '', send: bool = False, exc: bool = False) -> None:
        self._execute_error(self._TYPES_ERR.warning.value,
                           self._ICONS_ERR.warning.value,
                           self._COLOR_CODES_ERR.warning.value,
                           message, postfix, send, exc)

    def warning_not_done(self, message: str, postfix: str = '', send: bool = False, exc: bool = False) -> None:
        self._execute_error(self._TYPES_ERR.warning_not_done.value,
                           self._ICONS_ERR.warning_not_done.value,
                           self._COLOR_CODES_ERR.warning_not_done.value,
                           message, postfix, send, exc)

    def warning_error(self, message: str, postfix: str = '', send: bool = False, exc: bool = False) -> None:
        self._execute_error(self._TYPES_ERR.warning_error.value,
                           self._ICONS_ERR.warning_error.value,
                           self._COLOR_CODES_ERR.warning_error.value,
                           message, postfix, send, exc)

    def critical(self, message: str, postfix: str = '', send: bool = False, exc: bool = False) -> None:
        self._execute_error(self._TYPES_ERR.critical.value,
                           self._ICONS_ERR.critical.value,
                           self._COLOR_CODES_ERR.critical.value,
                           message, postfix, send, exc)

    def critical_fatal(self, message: str, postfix: str = '', send: bool = False, exc: bool = False) -> None:
        self._execute_error(self._TYPES_ERR.critical_fatal.value,
                           self._ICONS_ERR.critical_fatal.value,
                           self._COLOR_CODES_ERR.critical_fatal.value,
                           message, postfix, send, exc)
