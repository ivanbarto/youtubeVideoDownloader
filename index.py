from pytube import YouTube
from flask import Flask, send_file, request
from io import BytesIO

app = Flask(__name__)
app = Flask(__name__)

@app.route('/downloadTrailer', methods=['GET'])
def downloadTrailer():
    video_link = request.args.get("url")

    if (video_link != None) and (video_link):
        print("**********************************************")
        print("STARTING VIDEO DOWNLOAD...")
        print(video_link)
        print("**********************************************")
        buffer = BytesIO()
        url = YouTube(video_link)
        video = url.streams.get_by_itag(18)
        video.stream_to_buffer(buffer)
        buffer.seek(0)

    
        return send_file(
            buffer,
            as_attachment=True,
            attachment_filename=(url.title+".mp4"),
            mimetype="video/mp4",
        )
    else:
        return "video URL was not specified", 400


if __name__ == "__main__":
    app.run()
