AUTHOR = 'thlurte'
SITENAME = 'thlurte'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Colombo'

DEFAULT_LANG = 'en'
THEME = "/home/ahmed/lab/daedalus/themes/notsimple"
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

MENUITEMS = [
             ("about","about.html"),
             ("archive","archive.html"),
             ("tags","tags.html")]

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
