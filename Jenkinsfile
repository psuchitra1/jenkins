pipeline {
    agent any

    stages {
        stage('python') {
            steps {
                echo 'printing a name'
                bat 'python updateAPI.py'
            }
        }
        
        stage('flask') {
            steps {
                bat 'pip3 install flask'
            }
        }
    }
}
