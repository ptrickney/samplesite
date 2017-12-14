import pymongo
from pymongo import MongoClient


class HomeModel:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.memeit
        self.memes = self.db.memes

    def get_memes(self):
        memes = self.memes.find()
        return memes
