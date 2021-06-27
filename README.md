# AI MongoDB Template


### Run MongoDB
```bash
docker run --name mongodb-server -p 27017:27017 mongo
```

### Init some data
```bash
python src/init_db.py
```

### Get some data
```bash
python src/query_db.py
```

### Update some data
```bash
python src/update_db.py
```