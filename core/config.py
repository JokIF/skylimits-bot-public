from envparse import env
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent
CORE_DIR = Path(BASE_DIR) / "core"
ASSETS_DIR = Path(BASE_DIR) / "assets"

# links
manager_id = "6359994607"
manager_tag = "@n1LML"
manager_link = "https://t.me/n1LML"
review_group_tag = "@feedbackskyl"
in_stock_group_tag = "@skylimits00InStock"
how_to_link = "https://teletype.in/@skyl/howToDownloadPoizon"
FAQ_link = "https://teletype.in/@skyl/FAQ"

# const for price
markup_on_order = 1200
markup_on_rate = 0.9
markup_shirt_and_shorts = 350
markup_shoes_and_top = 1140
markup_sweatshirt_and_pants = 500

# env.read_envfile(BASE_DIR / '.env')

BOT_TOKEN = env("BOT_TOKEN")
REDIS_HOST = env("REDIS_HOST")
REDIS_PORT = env("REDIS_PORT")
REDIS_PASSWORD = env("REDIS_PASSWORD")
POSTGRESQL_HOST = env("POSTGRESQL_HOST") 
POSTGRESQL_USER = env('POSTGRESQL_USER')
POSTGRESQL_PASSWORD = env('POSTGRESQL_PASSWORD')
POSTGRESQL_PORT = env('POSTGRESQL_PORT')
POSTGRESQL_DB = env('POSTGRESQL_DB')
POSTGRESQL_URL = \
    f'postgresql://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}' \
    f':{POSTGRESQL_PORT}/{POSTGRESQL_DB}'
