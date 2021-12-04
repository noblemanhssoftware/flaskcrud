from src import app, db
from .models import Song, Podcast, Audiobook
from flask import jsonify, request

from .decorators import filetype_validator, body_validator


@app.route("/")
def home():
    return "Hello world"


@app.route("/create/<filetype>/", methods=["POST"])
@body_validator
@filetype_validator
def create(filetype):
    content = request.json
    if filetype == "song":
        name = content.get("name")
        duration = content.get("duration")
        data = Song(name=name, duration=duration)

    if filetype == "podcast":
        name = content.get("name")
        duration = content.get("duration")
        host = content.get("host")
        participants = content.get("participants")
        data = Podcast(
            name=name, duration=duration, host=host, participants=participants
        )

    if filetype == "audiobook":
        title = content.get("title")
        author = content.get("author")
        narrator = content.get("narrator")
        duration = content.get("duration")
        data = Audiobook(
            title=title, author=author, narrator=narrator, duration=duration
        )
    db.session.add(data)
    db.session.commit()
    return jsonify({"msg": f"{filetype} created", "data": data}), 201


@app.route("/<filetype>/<file_id>", methods=["PUT"])
@body_validator
@filetype_validator
def update(filetype, file_id):
    content = request.json
    if filetype == "song":
        data = Song.query.get(file_id)
        if data:
            name = content.get("name")
            duration = content.get("duration")
            data.name = name
            data.duration = duration
    db.session.commit()
    return jsonify({"msg": f"{filetype} updated", "data": data}), 200


@app.route("/<filetype>", methods=["GET"])
@filetype_validator
def get_all(filetype):
    if filetype == "song":
        data = Song.query.all()
        return jsonify({"msd": "all songs", "data": data})
    if filetype == "podcast":
        data = Podcast.query.all()
        return jsonify({"msd": "all podcasts", "data": data})
    if filetype == "audiobook":
        data = Audiobook.query.all()
        return jsonify({"msg": "all audiobooks", "data": data})


@app.route("/<filetype>/<file_id>", methods=["GET"])
@filetype_validator
def get_file(filetype, file_id):
    if filetype == "song":
        data = Song.query.get(file_id)
        if data:
            return jsonify({"msg": "song found", "data": data})
    if filetype == "podcast":
        data = Podcast.query.get(file_id)
        if data:
            return jsonify({"msg": "podcast found", "data": data})
    if filetype == "audiobook":
        data = Audiobook.query.get(file_id)
        if data:
            return jsonify({"msg": "audiobook found", "data": data})
    return jsonify({"error": f"'{filetype}' with id '{file_id}' not found"}), 404


@app.route("/<filetype>/<file_id>", methods=["DELETE"])
@filetype_validator
def delete_file(filetype, file_id):
    if filetype == "song":
        data = Song.query.get(file_id)
        if data:
            db.session.delete(data)
            return jsonify({"msg": "song deleted", "data": data})
    if filetype == "podcast":
        data = Podcast.query.get(file_id)
        if data:
            db.session.delete(data)
            return jsonify({"msg": "podcast deleted", "data": data})
    if filetype == "audiobook":
        data = Audiobook.query.get(file_id)
        if data:
            db.session.delete(data)
            return jsonify({"msg": "audiobook deleted", "data": data})
    return jsonify({"error": f"'{filetype}' with id '{file_id}' not found"}), 404

