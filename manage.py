from flask_script import Manager, Server
import main


# init manager object via app object
manager = Manager(main.app)
# create a new commands: server
# this command will be run the Flask develpment_env server
manager.add_command('runserver', Server())


@manager.shell
def make_shell_context():
    """create a python CLI

    return: Default import object
    type: `Dict`
    """
    # 确保有导入Flask app object，否则启动的CLI上下文中仍然没有app对象
    return dict(app=main.app)


if __name__ == '__main__':
    manager.run()
