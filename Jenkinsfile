pipeline {
    agent { docker { image 'python:3.8.7-buster' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test') {
            steps {
                sh 'python -m pytest'
            }
        }
    }
}
