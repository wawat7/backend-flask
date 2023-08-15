from configs.environment_config import get_environment_variables
from app import create_app

env = get_environment_variables()
app = create_app(env)

def main():
    app.run(port=8080, debug=True, host="0.0.0.0")

if __name__ == '__main__':
    main()
