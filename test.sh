COMMIT_SHA=$1

pytest --cov-report json:cov.json --cov=testier-playground/production_code testier-playground/tests


curl --fail-with-body -X POST "https://d0a4-46-117-101-250.ngrok-free.app/v1/ci-runs?commit_sha=$COMMIT_SHA&project_id=backend" -H "Authorization: gAAAAABlmT83KgI1_5zaWIa6zBGLnZEU0rqtMq-MPyoTqAyJTUwBQ6DgkVfGDgM1ZnvxhXRJcEzsqrq-nDywiQYUfPMRFQfpMWgGXpVRiXychixn-nMakbCRg6T72j17FGCeJq-ej8R2" -F report=@./cov.json
curl --fail-with-body -X POST "https://d0a4-46-117-101-250.ngrok-free.app/v1/ci-runs?commit_sha=$COMMIT_SHA&project_id=frontend" -H "Authorization: gAAAAABlmT83KgI1_5zaWIa6zBGLnZEU0rqtMq-MPyoTqAyJTUwBQ6DgkVfGDgM1ZnvxhXRJcEzsqrq-nDywiQYUfPMRFQfpMWgGXpVRiXychixn-nMakbCRg6T72j17FGCeJq-ej8R2" -F report=@./cov.json

