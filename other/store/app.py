import atexit

import db
import controllers.stockHandler as sh


class Application:
    data = dict({})
    name = "Inventory manager"

    def __init__(self, name: str, db_file: str = ""):
        self.name = name
        self.data = dict({})
        db_file = db_file

    def on_start(self):
        print(f"Running application: {self.name}")
        self.data = db.on_start()

        #test-> populate database        
        #sh.populate_database(self.data)
        for i, d in enumerate(self.data.items()):
            cat = d[0]
            items = d[1]
            print(f"[{cat}]")
            for art in items:
                print(art.cost)


    def on_shutdown(self):
        db.on_end()

    def get_data(self):
        return self.data

    def run(self):
        # init data
        self.on_start()
        act = 1
        while(act != 0):
            print("Application running")
            act = int(input('What should I do ? '))

app = Application("stock-management")


def exit_handler():
    print("About to exit")
    db.on_end(app.get_data())



atexit.register(exit_handler)

if __name__ == "__main__":    
    # run the application
    app.run()
