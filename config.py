import os

class Config(object):
    BOT_TOKEN = os.environ.get("8097210742:AAGqs1Jnov8GXVTPFBQM5KWcVPlFI7p0MiE")
    API_ID = int(os.environ.get("26697299"))
    API_HASH = os.environ.get("7326c7f4d7d714d782a130c77b09009c")
    VIP_USER = os.environ.get('VIP_USERS', '5168669934').split(',')
    VIP_USERS = [int() for user_id in VIP_USER]
