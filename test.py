import unittest

from src import app, db

TEST_DB = "test.db"


class APITest(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + TEST_DB
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def test_home(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_song(self):
        # test creattion of song
        response = self.app.post(
            "/create/song/", json={"name": "Mozart", "duration": 200}
        )
        self.assertEqual(response.status_code, 201)
        song_id = response.json["data"]["id"]

        # test get all songs
        response = self.app.get("/song")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json["data"]), 1)

        # test get song by id
        response = self.app.get(f"/song/{song_id}")
        self.assertEqual(response.status_code, 200)

        # test get song by non existing id
        response = self.app.get("/song/non_id")
        self.assertEqual(response.status_code, 404)

        # test incorrect duration
        response = self.app.post(
            "/create/song/", json={"name": "Mozart", "duration": "two hundred"}
        )
        self.assertEqual(response.status_code, 400)

        # test incomplete payload
        response = self.app.post("/create/song/", json={"name": "Mozart"})
        self.assertEqual(response.status_code, 400)

        # test delete song by id
        response = self.app.delete(f"/song/{song_id}")
        self.assertEqual(response.status_code, 200)

        # test delete song by id
        response = self.app.delete("/song/non_id")
        self.assertEqual(response.status_code, 404)

    def test_podcast(self):
        # test creattion of podcast
        response = self.app.post(
            "/create/podcast/",
            json={
                "name": "Talk me",
                "duration": 200,
                "host": "mike",
                "participants": "Cyril, Joe, Jane",
            },
        )
        self.assertEqual(response.status_code, 201)
        podcast_id = response.json["data"]["id"]

        # test get all podcasts
        response = self.app.get("/podcast")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json["data"]), 1)

        # test get song by id
        response = self.app.get(f"/podcast/{podcast_id}")
        self.assertEqual(response.status_code, 200)

        # test get song by non existing id
        response = self.app.get("/podcast/non_id")
        self.assertEqual(response.status_code, 404)

        # test incorrect duration
        response = self.app.post(
            "/create/podcast/", json={"name": "Mozart", "duration": "two hundred"}
        )
        self.assertEqual(response.status_code, 400)

        # test incomplete payload
        response = self.app.post(
            "/create/podcast/", json={"name": "Talk me", "duration": 200}
        )
        self.assertEqual(response.status_code, 400)

        # test delete song by id
        response = self.app.delete(f"/podcast/{podcast_id}")
        self.assertEqual(response.status_code, 200)

        # test delete song by id
        response = self.app.delete("/podcast/non_id")
        self.assertEqual(response.status_code, 404)

    def test_audiobook(self):
        # test creattion of audiobook
        response = self.app.post(
            "/create/audiobook/",
            json={
                "title": "48 Laws of Power",
                "duration": 5000,
                "author": "Robert Greene",
                "narrator": "Sydney",
            },
        )
        self.assertEqual(response.status_code, 201)
        audiobook_id = response.json["data"]["id"]

        # test get all audiobooks
        response = self.app.get("/audiobook")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json["data"]), 1)

        # test get audiobook by id
        response = self.app.get(f"/audiobook/{audiobook_id}")
        self.assertEqual(response.status_code, 200)

        # test get audiobook by non existing id
        response = self.app.get("/audiobook/non_id")
        self.assertEqual(response.status_code, 404)

        # test incorrect duration
        response = self.app.post(
            "/create/audiobook/",
            json={"title": "48 Laws of Power", "duration": "two hundred"},
        )
        self.assertEqual(response.status_code, 400)

        # test incomplete payload
        response = self.app.post(
            "/create/podcast/",
            json={
                "title": "48 Laws of Power",
                "duration": 5000,
                "author": "Robert Greene",
            },
        )
        self.assertEqual(response.status_code, 400)

        # test delete audiobook by id
        response = self.app.delete(f"/audiobook/{audiobook_id}")
        self.assertEqual(response.status_code, 200)

        # test delete audiobook by id
        response = self.app.delete("/audiobook/non_id")
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
