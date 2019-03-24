from connexion.resolver import RestyResolver
import connexion


if __name__ == '__main__':
    app = connexion.App(__name__, 9090, specification_dir='openapi/swagger/')
    app.add_api('swagger.yaml', resolver=RestyResolver('api'))
    app.run()
