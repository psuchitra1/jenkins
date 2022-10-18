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
                bat 'pip3 install Flask-Cors'
            }
        }
        stage('flask') {
            steps {
                bat 'pip3 install flask'
            }
        }
    }
}
