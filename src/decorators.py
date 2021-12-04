from functools import wraps
from flask import jsonify, request

from .utils import validate_duration, name_length, validate_participants


def filetype_validator(func):
    @wraps(func)
    def valid(*args, **kwargs):
        filetype = locals()["kwargs"]["filetype"].lower()
        if filetype not in ("song", "podcast", "audiobook"):
            return jsonify({"error": f"{filetype} is not recognized"}), 400
        return func(*args, **kwargs)

    return valid


def body_validator(func):
    @wraps(func)
    def valid(*args, **kwargs):
        filetype = locals()["kwargs"]["filetype"].lower()
        content = request.json
        if filetype == "song":
            name = content.get("name", None)
            duration = content.get("duration", None)
            if None in (name, duration):
                return jsonify({"error": "'name' and 'duration' required"}), 400
            if not validate_duration(duration):
                return jsonify({"error": "'duration' must be a positive integer"}), 400
            if not name_length(name):
                return jsonify({"error": "'name' must not be longer than 100"}), 400
        if filetype == "podcast":
            name = content.get("name", None)
            duration = content.get("duration", None)
            host = content.get("host", None)
            participants = content.get("participants", None)

            if None in (name, duration, host, participants):
                return (
                    jsonify(
                        {
                            "error": "'name', 'duration', 'hosts', 'participants' required"
                        }
                    ),
                    400,
                )
            if not name_length(name):
                return jsonify({"error": "'name' must not be longer than 100"}), 400
            if not validate_duration(duration):
                return jsonify({"error": "'duration' must be a positive integer"}), 400
            if not name_length(host):
                return jsonify({"error": "'host' must not be longer than 100"}), 400
            if not validate_participants(participants):
                return (
                    jsonify(
                        {
                            "error": "'participant' must not be more than 10 and each participant name must not be more than 100 characters"
                        }
                    ),
                    400,
                )
        if filetype == "audiobook":
            title = content.get("title", None)
            author = content.get("author", None)
            narrator = content.get("narrator", None)
            duration = content.get("duration", None)

            if None in (title, author, narrator, duration):
                return (
                    jsonify(
                        {"error": "'title', 'duration', 'author', 'narrator' required"}
                    ),
                    400,
                )
            if not name_length(title):
                return jsonify({"error": "'title' must not be longer than 100"}), 400

            if not name_length(author):
                return jsonify({"error": "'author' must not be longer than 100"}), 400

            if not name_length(narrator):
                return jsonify({"error": "'narrator' must not be longer than 100"}), 400

        return func(*args, **kwargs)

    return valid

