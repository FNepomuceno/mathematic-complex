pipeline {
    agent { docker { image 'python:3.8.7-buster' } }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                }
            }
        }
        stage('test') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python -m pytest --junitxml build/reports/test-results.xml'
                }
            }
        }
    }
    post {
        always {
            junit 'build/reports/test-results.xml'
        }
    }
}
