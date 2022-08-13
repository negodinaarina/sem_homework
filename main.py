from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, SubmitField, SelectField, validators
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor, CKEditorField
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'jfjc4u5ueqruchuw008550985'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# db.create_all()


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    cover_img = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=False)
    page_img = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    lenght = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(250), nullable=False)
# db.create_all()


class EditForm(FlaskForm):
    title = StringField('title', [validators.Length(min=5)])
    subtitle = StringField('subtitle', [validators.Length(min=20)])
    cover_img_url = StringField('main image url', [validators.Length(min=5)])
    page_img_url = StringField('second image url', [validators.Length(min=5)])
    description = CKEditorField('description', [validators.Length(min=40)])
    rating = StringField('rating', [validators.Length(min=1)])
    time_reading = StringField('time for reading', [validators.Length(min=1)])
    type = StringField('type', [validators.Length(min=1)])
    submit = SubmitField('submit')


class FilterForm(FlaskForm):
    filters = SelectField(u'Filters', choices=[('all', 'все'), ('fi', 'фильмы'), ('pe', 'персоны')])
    submit = SubmitField('найти')


@app.route('/')
def main_page():
    return render_template('index.html', current_user=current_user)


@app.route('/articles', methods=["GET", "POST"])
def articles():
    filter = FilterForm()
    if request.method == "POST":
        data = filter.filters.data
        if data != 'all':
            posts = BlogPost.query.filter_by(type=data).all()
            return render_template('articles.html', posts=posts, form=filter, current_user=current_user)
    posts = db.session.query(BlogPost).all()
    return render_template('articles.html', posts=posts, form=filter, current_user=current_user)


@app.route('/article/<int:id>')
def article(id):
    post = BlogPost.query.get(id)
    title = post.title
    alp = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM '
    eng_str = ''
    jp_str = ''
    for el in title:
        if el in alp:
            eng_str += el
        else:
            jp_str += el
    return render_template('article.html', post=post, eng=eng_str, jp=jp_str, current_user=current_user)


@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    post = BlogPost.query.get(id)
    form = EditForm(title=post.title, subtitle=post.subtitle, cover_img_url=post.cover_img,
                    page_img_url=post.page_img, description=post.description, rating=post.rating, time_reading=post.lenght, type=post.type)
    if request.method == 'POST':
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.cover_img = form.cover_img_url.data
        post.page_img = form.page_img_url.data
        post.description = form.description.data
        post.rating = form.rating.data
        post.lenght = form.time_reading.data
        post.type = form.type.data
        db.session.commit()
        return redirect(url_for('articles'))
    return render_template('edit.html', form=form, current_user=current_user)


@app.route('/create', methods=["GET", "POST"])
def create():
    form = EditForm()
    if request.method == 'POST':
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            cover_img=form.cover_img_url.data,
            page_img=form.page_img_url.data,
            description=form.description.data,
            rating=form.rating.data,
            lenght=form.time_reading.data,
            type=form.type.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('articles'))
    return render_template('edit.html', form=form, current_user=current_user)


@app.route('/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('articles'))


@app.route('/login', methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        user = User.query.filter_by(name=request.form.get('name')).first()
        if request.form.get('password') == user.password:
            login_user(user)
            return redirect(url_for('main_page'))
        else:
            error = 'Wrong login data'
            return render_template('login.html', error=error, current_user=current_user)
    return render_template('login.html', current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_page'))


if __name__ == '__main__':
    app.run(debug=True)


