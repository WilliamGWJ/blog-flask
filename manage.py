from flask_script import Manager, Server
from . import main


manager = Manager(main.app)
