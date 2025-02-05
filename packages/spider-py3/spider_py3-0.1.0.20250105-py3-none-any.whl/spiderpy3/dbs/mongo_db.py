from typing import Any, Optional, List, Dict
from urllib.parse import quote_plus
from pymongo import MongoClient
from pymongo.synchronous.database import Database

from spiderpy3.dbs.db import DB


class MongoDB(DB):
    def __init__(
            self,
            *args: Any,
            host: str = "localhost",
            port: int = 27017,
            username: Optional[str] = None,
            password: Optional[str] = None,
            dbname: str,
            **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)

        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.dbname = dbname

    @staticmethod
    def get_client(
            *,
            host: str = "localhost",
            port: int = 27017,
            username: Optional[str] = None,
            password: Optional[str] = None,
    ) -> MongoClient:
        if username and password:
            uri = "mongodb://%s:%s@%s:%s" % (quote_plus(username), quote_plus(password), host, port)
        else:
            uri = "mongodb://%s:%s" % (host, port)
        client = MongoClient(uri)
        return client

    @staticmethod
    def get_db(client: MongoClient, dbname: str) -> Database:
        db = client[dbname]
        return db

    def _open(self) -> None:
        self.client = self.get_client(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password
        )
        self.db = self.get_db(self.client, self.dbname)

    @staticmethod
    def close_client(client: MongoClient) -> None:
        if client:
            client.close()

    def _close(self) -> None:
        self.close_client(self.client)

    def add(self) -> None:
        pass

    def delete(self) -> None:
        pass

    def update(self) -> None:
        pass

    def query(self) -> List[Dict[str, Any]]:
        pass
