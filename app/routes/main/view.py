from app.routes.main import bp


@bp.route('/', methods=['GET', 'POST'])
def main():
    return "Hello world"
