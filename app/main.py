from run import db

def run():
    pass

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    run()