from models.Article import Article

def populate_database(data: dict = {}):
    print(f">>>> Type of data argument: {type(data)}")
    d = [("art-name", "art-maker", "art-model", 1250 * i, 3 * i, "wearables") for i in range(0,10, 1)]
    for idx, art in enumerate(d):
        #if(data[f'{art[5]}']):
        if(len(data.keys()) == 0 ):
            data[f'{art[5]}'] = []
        else:
            if(data[f'{art[5]}']):
                data[art[5]].append(Article(art[0], art[1], art[2], art[3], art[4], art[5]))
            else:
                data[art[5]] = []
                data[art[5]].append(Article(art[0], art[1], art[2], art[3], art[4], art[5]))