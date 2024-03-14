pipeline {
    agent any

    environment {
        // Define the Docker image name
        IMAGE_NAME = 'tests'
        TAG = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def customImage = docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('Run API Test') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}:${TAG}").run('python world_page_test.py')
                }
            }
        }

        stage('Run world test') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}:${TAG}").inside {
                        sh 'python world_page_test.py'
                    }
                }
            }
        }
    }
}
