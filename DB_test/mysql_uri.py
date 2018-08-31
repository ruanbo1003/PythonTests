


from urllib.parse import urlparse
from playhouse.db_url import parse

def mysql_uri():
    db = parse("mysql://root:root@192.168.1.106/irm")
    print(dir(db))
    print(db)
    # print(db.hostname, db.port, db.username, db.password, db.path)

    print(db.get('database'))


def redis_uri():
    str = "redis://192.168.1.106:6379/1"
    uri = parse(str)
    print(uri)


if False:
    db2 = parse('mysql://root:88meeting@meeting.ckm8z9g0pwyk.ap-southeast-1.rds.amazonaws.com:3307/meeting')
    print(db2)

    print(type(db2.get('port')))
    print(type(db2.get('port', 3306)))

    print(db2.get('port', 3306))

if __name__ == "__main__":
    redis_uri()
