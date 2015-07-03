from flask_script import Manager,commands
from phlaskr import application
print dir(application)
manager = Manager(application)


manager.add_command('urls',commands.ShowUrls())

if __name__ == "__main__":
    manager.run()
