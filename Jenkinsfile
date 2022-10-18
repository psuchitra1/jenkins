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
                bat 'pip install Flask_Cors'
            }
        }
        stage('flask') {
            steps {
                bat 'pip install flask'
            }
        }
    }
}
