import flask
from flask import request,url_for,redirect
from flask import make_response,send_file
from wordcloud_zju import word_spliter,wordclouder


# Create the application.
APP = flask.Flask(__name__)


@APP.route('/',methods=['GET', 'POST'])
def index():
    """ 显示可在 '/' 访问的 index 页面
    """
    return redirect(url_for('upload'))

@APP.route('/upload',methods=['GET', 'POST'])
def upload():
    err = None
    if request.method == "POST":
        pic = request.files['uploadPic']
        text = request.form['wordStr']
        pic_path = "./static/pic/"+pic.filename
        pic.save(pic_path)
        generate_wordcloud(text,pic_path)
        response = make_response(send_file(pic_path))
        response.headers["Content-Disposition"] = "attachment; filename=wordcloud.jpg;"
        return response
        # return flask.render_template('wordcloud.html',pic_name = 'pic/'+pic.filename)
    else:
        err = "post method required"
    return  flask.render_template('upload.html',error=err)

# @APP.route('/wordcloud',methods=['GET', 'POST'])
# def showPic():
#     response = make_response()
#     return flask.render_template('wordcloud.html')

def generate_wordcloud(text,pic):
    sp_word = word_spliter(text)
    words = sp_word.split_word()
    g_word = wordclouder(words,pic)
    g_word.word_cloud()


if __name__ == '__main__':
    APP.debug=True
    APP.run(port=8521)