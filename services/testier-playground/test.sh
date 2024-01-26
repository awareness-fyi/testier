source ../venv/bin/python
pytest --cov-report json:cov.json --cov=production_code tests

python ../src/ci.py --pull-request 1 --repository awareness-fyi/testier-playground -f cov.json
