from app import app, db
from app.forms import PostForm
from app.models import Post
from flask import render_template, flash, redirect, url_for, request

@app.route('/cu', methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('explore'))
    return render_template('cu.html', title='Create Post',
                            form=form, type = 'Create form')

@app.route('/', methods=['GET', 'POST'])
@app.route('/explore')
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('cu.html', title='Explore', posts=posts.items,
                           next_url=next_url, prev_url=prev_url)

@app.route('/<int:post_id>/edit', methods=['GET', 'POST'])
def edit(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title_ = form.title.data
        body_ = form.body.data
        post = Post.query.filter_by(id=post_id).first()
        post.title = title_
        post.body = body_     
        db.session.add(post)
        db.session.commit()
        flash('Your post is edited :)')
        return redirect(url_for('explore'))
    return render_template('cu.html', title = 'Create Post',
                            form = form, type = 'Update form')




@app.route("/<int:post_id>/delete", methods=['POST', 'GET', 'DELETE'])

def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted!')
    return redirect(url_for('explore'))