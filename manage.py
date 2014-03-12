from flask.ext.script import Manager

from teela import init
from teela.extensions import db
from teela.frontend import Message

app = init()
manager = Manager(app)


@manager.command
def run():
    """ Run locally, host and port set by configuration. """
    app.run()


@manager.command
def setup():
    """ Init database and test message. """
    db.drop_all()
    db.create_all()

    message = Message(text=u'Hello World.')

    db.session.add(message)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
