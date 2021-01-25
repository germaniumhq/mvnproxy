from mvnproxy import config
from mvnproxy import mainapp

app = mainapp.app
application = app


def launch():
    app.run(host=config.host, port=config.port, debug=True)


if __name__ == "__main__":
    launch()
