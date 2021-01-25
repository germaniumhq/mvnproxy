import uvicorn

from mvnproxy import mainapp, config

app = mainapp.app
application = app


def launch():
    # app.run(host=config.host, port=config.port, debug=True)
    uvicorn.run(app, host=config.host, port=config.port)


if __name__ == "__main__":
    launch()
