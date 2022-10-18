pipeline {
    agent any

    stages {
        stage('python') {
            steps {
                bat 'python updateAPI.py'
            }
        }
        stage('install') {
            steps {
                bat 'pip install python-jenkins'
            }
        }
        stage('flask') {
            steps {
                bat 'pip install flask'
            }
        }
    }
}
