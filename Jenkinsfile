pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh('docker build -t sicei-${GIT_BRANCH}:1.1.0-${BUILD_NUMBER} .')
                sh('docker image ls')
            }
        }
        stage('Run Docker Container') {
            steps {
                sh('docker run -d -p 8080:8080 sicei-${GIT_BRANCH}:1.1.0-${BUILD_NUMBER}')
                sh('docker container ls')
            }
        }
    }
}