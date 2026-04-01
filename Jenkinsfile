pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Cloning repository...'
                git 'https://github.com/sashank703-cmyk/jenkins-project.git'
            }
        }

        stage('Deploy App') {
            steps {
                echo 'Deploying using Docker Compose...'
                sh '''
                docker-compose down || true
                docker-compose up -d --build
                '''
            }
        }
    }
}
