class Config():
    pass


class ProdConfig():
    pass


class DevConfig():
    # open debug
    DEBUG = True
    SQLALCHMEY_DATABASE_URI = 'mysql+pymysql://root:william@127.0.0.1:3306/william'