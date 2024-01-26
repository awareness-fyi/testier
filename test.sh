COMMIT_SHA=$1


CHANGED_SERVICES=$(git diff ..main --name-only | xargs -L1 dirname | grep -vw . | sed 's/^services\///' | sed 's/\/.*$//' | sort | uniq)
echo "  *  Changed services: $CHANGED_SERVICES"
TEMP_PYTHONPATH=$PYTHONPATH
if [[ -n "${CHANGED_SERVICES}" ]]; then
  cd services || exit
  echo "${CHANGED_SERVICES}" | while IFS= read -r SERVICE; do
    pwd
    echo "  *  Testing '$SERVICE'"
    cd "$SERVICE" || exit
    PYTHONPATH=$TEMP_PYTHONPATH:$(pwd)/$SERVICE
    export PYTHONPATH
    pytest --cov-report json:cov.json --cov=src tests
    curl --fail-with-body -X POST "https://c2cc-46-117-106-193.ngrok-free.app/v1/ci-runs?commit_sha=$COMMIT_SHA&project_id=$SERVICE&project_glob=services/$SERVICE/*" -H "Authorization: gAAAAABlmT83KgI1_5zaWIa6zBGLnZEU0rqtMq-MPyoTqAyJTUwBQ6DgkVfGDgM1ZnvxhXRJcEzsqrq-nDywiQYUfPMRFQfpMWgGXpVRiXychixn-nMakbCRg6T72j17FGCeJq-ej8R2" -F report=@./cov.json
    echo "\nDone testing $SERVICE"
    cd ../

  done
fi
