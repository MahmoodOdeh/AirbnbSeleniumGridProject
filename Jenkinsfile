pipeline {
    agent any

    environment {
        // Define the Docker image name
        IMAGE_NAME = 'tests'
        TAG = 'latest'
    }

    stages {
        stage('Debug') {
            steps {
                echo 'Starting parallel execution...'
            }
        }

        stage('Run Tests in Parallel') {
            steps {
                script {
                    parallel(
                        'API Test': {
                            echo 'Running API test...'
                            bat "docker rm -f api_test || true"
                            bat "docker run --name aram ${IMAGE_NAME}:${TAG} python tankerkoenig_stats_api_test.py"
                        },
                        'Change Language': {
                            echo 'Running change language test...'
                            bat "docker rm -f UI_test || true"
                            bat "docker run --name UI_test ${IMAGE_NAME}:${TAG} python world_page_test.py"
                        }
                    )
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // bat "docker rmi ${IMAGE_NAME}:${TAG}"
        }
    }
}
