pipeline {
    agent any

    stages {
        stage('python') {
            steps {
                echo 'printing a name'
                bat 'python updateAPI.py'
            }
        }
        stage('install') {
            steps {
                bat 'pip3 install -U flask-cors'
            }
        }
        stage('flask') {
            steps {
                bat 'pip3 install flask'
            }
        }
    }
}
