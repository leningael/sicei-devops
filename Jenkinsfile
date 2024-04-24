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
                sh('docker container stop sicei-container || true')
                sh('docker container rm sicei-container || true')
                sh('docker run -dp 8000:8000 --name "sicei-container" sicei-${GIT_BRANCH}:1.1.0-${BUILD_NUMBER}')
                sh('docker container ls')
            }
        }
    }
}