from flask import render_template

from app.routes.main import bp


@bp.route('/', methods=['GET', 'POST'])
def main():
    colors = ['Black', 'Blue', 'Purple']
    return render_template('base.html', colors=colors)
