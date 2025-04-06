# Simple framework for easy-to-read display of logs with save to db redis and sending notifications in telegram.
  
Once I couldn't find a simple framework that does 3 things that are important to me:  
* marking messages with color in the terminal,
* saving logs by day to the database redis,
* sending important notifications in telegram.
  
Then it was created LogsWeasel.  
  
_ _ _
```
log = LogsWeasel(settings={
    'redis_connection': {
        'db': {{id_database, default that 0, int}},
        'host': {{redis_host, str}}),
        'port': {{number_of_port, int}},
        'username': {{username, str}},
        'password': {{password, str}},
    'redis_files': {
        'prefix_file': 'logs_',
        'frequency': 'day'},
    'telegram_token': {{you_tg_token, str}},
    'users_list': {{[tg_id_int_1, tg_id_int_2, ...], list with int}})
```
_ _ _
## Example use:
```
from logsweasel import LogsWeasel

log = LogsWeasel(settings={
    'redis_connection': {
        'db': int(os.getenv('redis_db')),
        'host': os.getenv('redis_host'),
        'port': int(os.getenv('redis_port')),
        'username': os.getenv('redis_username'),
        'password': os.getenv('redis_password')},
    'redis_files': {
        'prefix_file': 'logs_',
        'frequency': 'day'},
    'telegram_token': os.getenv('telegram_token'),
    'users_list': [int(os.getenv('user_tgid'))]})


def hello_world(def_name='Hello World'):
    try:
        log.info_start(def_name) # message starting
        message = 'Hello World #1'
        print(message)
        time.sleep(3) # working...
        if message == 'Hello World #1':
            log.info_done(def_name, send=True) # done message
        else:
            log.warning(def_name) # not done message
    except Exception:
        log.critical(def_name) # finish with error


hello_world()
```
_ _ _

where:
* redis_connection - settings for your database redis.

redis_files:
* prefix_file - name of your save in db redis. Default key in db redis: {prefix_file}{date}
* frequency - you can use 3 types frequency for save logs in new key: day, week, month.

* telegram_token - token to initialize your bot to send notifications
* users_list - list of user IDs to whom notifications will be sent

### * You can find out your telegram ID, for example, using a bot @my_id_bot

### * You can also save some logs in a separate file (for even better readability), for this you can use the following construction:
log.info(def_name, postfix='another_key')  
You save the key like this: {prefix_file}{date}{postfix}  
  
### * If you do not want to use redis, write None in key redis_connection
### * If you do not want to use telegram, write None in key telegram_token

_ _ _
## Default methods for save logs:
  
Information records/notifications. Marked in green in the terminal  
log.info() - default message  
log.info_start() - usually used when starting a function  
log.info_done() - usually used when a function has completed successfully  
log.info_not_done() - used when a function has not completed  
  
Notices to watch out for. Marked in yellow in the terminal.  
log.warning() - important low  
log.warning_not_done() - important medium  
log.warning_error() - important high  
  
Critical notices. They have the ability to save in the terminal full descriptions of the errors that have occurred.  
log.critical() - error with important high  
log.critical_fatal() - error with important very high, х_х  
  
### * default argument for warning/critical - exc=True, that add traceback message
### ** Use telegram bot notifications with great care. A large number of users in the send list will affect the performance of the program as a whole!
