pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/badal1e/calculatorr-app.git'

            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t calculator-app .'
            }
        }

        stage('Run Tests in Container') {
            steps {
                bat 'docker run --rm calculator-app'
            }
        }
        stage('Check AWS & SAM') {
            steps {
                bat 'aws --version'
                bat 'sam --version'
            }
        }

    }
}

