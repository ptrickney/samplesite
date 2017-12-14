import web
import pymongo
from pymongo import MongoClient
from Models import HomeModel


urls = (
    '/', 'home'
)

# Uses the MainLayout template
render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())

# Classes/Routes


class home:
    def GET(self):
        memedb = HomeModel.HomeModel()
        memes = memedb.get_memes()

        return render.home(memes)
        # uses the page 'home' on the MainLayout template


if __name__ == "__main__":
    app.run()
