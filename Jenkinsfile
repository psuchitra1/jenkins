pipeline {
    agent any

    stages {
        stage('python') {
            steps {
                bat 'python updateAPI'
            }
        }
        stage('install') {
            steps {
                bat 'pip install flask_cors'
            }
        }
        stage('flask') {
            steps {
                bat 'pip install flask'
            }
        }
    }
}
