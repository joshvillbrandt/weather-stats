# weather-stats

An exploration in using APIs in Python with docker and tests.

## Topics

1. git
2. docker
3. downloading data (requests library)
4. testing, mocking (pytest library)

## Usage

Clone the repository:

```bash
mkdir -p ~/workspace
cd ~/workspace
git clone https://github.com/joshvillbrandt/weather-stats.git
cd weather-stats
```

Then run docker:

| `docker-compose up` | Run the app and quit when the app exits. |
| `docker-compose run app /bin/bash` | Start the container and open a shell. |
| `docker-compose run app pytest -rA` | Run the tests. |
| `docker-compose run app flake8 app tests` | Run the linter. |
