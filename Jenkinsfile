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
                            bat "docker run --name api_test_runner ${IMAGE_NAME}:${TAG} tankerkoenig_stats_api_test.py"
                            bat "docker rm api_test_runner"
                        },
                        'Change Language': {
                            echo 'Running change language test...'
                            bat "docker run --name performance_test ${IMAGE_NAME}:${TAG} python world_page_test.py"
                            bat "docker rm performance_test"
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
