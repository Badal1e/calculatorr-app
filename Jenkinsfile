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

        stage('SAM Build (Package for AWS)') {
            steps {
                bat 'sam build'
            }
        }

        stage('Deploy to AWS (CD)') {
            steps {
                bat 'sam deploy --no-confirm-changeset --no-fail-on-empty-changeset'
            }
        }
    }
}

