COMMIT_SHA=$1


CHANGED_SERVICES=$(git diff ..main --name-only | xargs -L1 dirname | grep -vw . | sed 's/^services\///' | sed 's/\/.*$//' | sort | uniq)
echo "  *  Changed services: $CHANGED_SERVICES"
if [[ -n "${CHANGED_SERVICES}" ]]; then
  cd services || exit
  for SERVICE in $CHANGED_SERVICES; do
    if [ -d "$SERVICE" ]; then
      echo "  *  Testing '$SERVICE'"
      cd "$SERVICE" || exit
      pytest --cov-report json:cov.json --cov=src tests
      curl --fail-with-body -X POST "https://bb80-46-117-106-193.ngrok-free.app/v1/ci-runs?commit_sha=$COMMIT_SHA&project_id=$SERVICE&project_glob=services/$SERVICE/*" -H "Authorization: gAAAAABlmT83KgI1_5zaWIa6zBGLnZEU0rqtMq-MPyoTqAyJTUwBQ6DgkVfGDgM1ZnvxhXRJcEzsqrq-nDywiQYUfPMRFQfpMWgGXpVRiXychixn-nMakbCRg6T72j17FGCeJq-ej8R2" -F report=@./cov.json
      echo "Done testing $SERVICE"
      cd ../
    fi
  done
fi
