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
                bat "docker run --name api_test_runner ${IMAGE_NAME}:${TAG} python world_page_test.py"
                bat "docker rm api_test_runner"
            }
        }

        stage('Run world test') {
            steps {
                bat "docker run --name python world_page_test ${IMAGE_NAME}:${TAG} python python world_page_test