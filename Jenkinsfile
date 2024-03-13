pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'

                bat 'pip install -r requirements.txt'

            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'

                bat 'python -m unittest /test/world_page_test.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'


            }
        }
    }
}