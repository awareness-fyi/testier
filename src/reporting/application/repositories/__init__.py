from mongoengine import connect

from infrastructure.config import Config

# connection_string = "mongodb+srv://podj:ph3baivHsadL7lrt@prod.ynbnlzv.mongodb.net/?retryWrites=true&w=majority"
connect(Config.DB_CONNECTION_STRING)
