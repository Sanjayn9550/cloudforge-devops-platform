pipeline {
    agent any

    environment {
        IMAGE_NAME = "cloudforge-app:v1"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Sanjayn9550/cloudforge-devops-platform.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME ./app'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'docker save cloudforge-app:v1 | sudo k3s ctr images import -'
                sh 'sudo k3s kubectl apply -f k8s/deployment.yaml'
                sh 'sudo k3s kubectl apply -f k8s/service.yaml'
            }
        }
    }
}
