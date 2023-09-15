
REPOSITORY=$1
PR_NUMBER=$2

pytest --cov-report json:cov.json --cov=testier-playground/production_code testier-playground/tests
python src/ci.py --pull-request $PR_NUMBER --repository $REPOSITORY -f cov.json
