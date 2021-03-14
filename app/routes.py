from flask import request,jsonify
from app import app
from app.models import (Song, Podcast, AudioBook, song_schema, songs_schema,
 podcast_schema, podcasts_schema, audiobook_schema, audiobooks_schema )
from datetime import datetime
from app import db
from werkzeug.exceptions import InternalServerError



@app.route("/song", methods=["POST"])
def song():
    try:
        data = request.get_json()
        result = Song.query.filter_by(name_of_song=data["name_of_song"]).first()
        if result:
            if result.name_of_song: 
                return jsonify({"message":"Song already exist"}), 409
            
        new_song = Song(name_of_song=data['name_of_song'], duration_of_song=data['duration_of_song'],uploaded_time=datetime.utcnow())
        db.session.add(new_song)
        db.session.commit()
        data = song_schema.dump(new_song)
        return jsonify({ "Data":data, "message": "Song created successfully"}), 201
        
    except Exception as e:

        return jsonify({'error_msg': str(e)}), 400
    except InternalServerError as e:
        return jsonify({'error_msg': str(e)}), 500

@app.route("/song/<int:id>", methods=["GET"])
def get_a_song(id):
    song = Song.query.get(id)     
    if song:
            # return a serialised data
        result = song_schema.dump(song)
        return jsonify({"Song" : result }), 200   
    return jsonify({"msg" : "Song not found" }), 404  

@app.route("/song", methods=["GET"])
def get_all_songs():
    try:
        song = Song.query.all()     
        if song:
                # return a serialised data
            result = songs_schema.dump(song)
            return jsonify({"Songs" : result }), 200 

    
    except Exception as e:

        return jsonify({'error_msg': str(e)}), 400
    except InternalServerError as e:
        return jsonify({'error_msg': str(e)}), 500


@app.route("/song/<int:id>", methods=["PUT"])
def update_a_song(id):

    try:
        song = Song.query.get(id)
        if song:
            song.name_of_song = request.json['name_of_song']
            song.duration_of_song = request.json['duration_of_song']
            db.session.commit()
            return jsonify({"msg": "Song updated successfully"}), 200
        else:
            return  jsonify({"msg": "Song not found"}), 404
      
    except Exception as e:

        return jsonify({'error_msg': str(e)}), 400
    except InternalServerError as e:
        return jsonify({'error_msg': str(e)}), 500

@app.route("/song/<int:id>", methods=["DELETE"])
def delete_a_song(id):
    try:
        song = Song.query.get(id)
        if song:
            db.session.delete(song)
            db.session.commit()
            return jsonify({'msg': 'Song deleted successfully'}), 200
        else:
            return  jsonify({"msg": "Song not found"}), 404
   
    except Exception as e:

        return jsonify({'error_msg': str(e)}), 400
    except InternalServerError as e:
        return jsonify({'error_msg': str(e)}), 500


