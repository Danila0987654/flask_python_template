from flask import render_template

from app.routes.main import bp


@bp.route('/', methods=['GET', 'POST'])
def main():
    colors = ['Black', 'Blue', 'Purple']
    return render_template('content/main.html', colors=colors)


@bp.route('/about')
def about():
    return render_template('content/about.html')
