class config:
    BOT_TOKEN = "1406408953:AAHjcYwC1Jsu4bYCwg4cO4EIBesXmwSNJTQ"
    APP_ID = "1438968"
    API_HASH = os.environ.get('API_HASH')
    DATABASE_URL = os.environ.get('DATABASE_URL')    
    SUDO_USERS = os.environ.get('SUDO_USERS')
    SUPPORT_CHAT_LINK = "t.me/moedyiu"
    DOWNLOAD_DIRECTORY = "./downloads/"
    PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""


class BotCommands:
  Authorize = ['auth', 'start']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  Channelmyanmar = ['cm']
  Mmsubtitles = ['mmsub']
  Vidsearch = ['vid']
  Linkgen = ['cmgen']
  Logo = ['logo']
  Javgen = ['javgen']
  Test = ['test']
class Messages:
    
    NOT_AUTH = f"🔑 **You have not authenticated me to upload to any account.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    START = "တင်‌ပေးနေပါပြီနော် "
    DOWNLOADED_SUCCESSFULLY = "📤 **mmsub.co...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    
