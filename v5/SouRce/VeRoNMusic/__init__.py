from VeRoNMusic.core.bot import KIMBot
from VeRoNMusic.core.dir import dirr
from pyromod import listen
from VeRoNMusic.core.cookies import save_cookies
from VeRoNMusic.core.userbot import Userbot
from VeRoNMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

save_cookies()


# Load Sudo Users from DB
sudo()
# Bot Client
app = KIMBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
