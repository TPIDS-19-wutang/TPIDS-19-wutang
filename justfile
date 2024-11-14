list:
  cat justfile

local-up:
  docker-compose up

# Setup Python venv
create-virtual-env:
  pyenv install -s 3.13.0 && \
  pyenv virtualenv 3.13.0 wutang-api && \
  pyenv local wutang-api

destroy-virtual-env:
  pyenv virtualenv-delete -f wutang-api

install:
  poetry install

run-api:
  $(cd backend && poetry run flask run -p 5001)


