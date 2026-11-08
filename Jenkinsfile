pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                bat 'wsl docker build -t yentanmayi/movie-app:latest .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                echo "Pushing to Docker Hub..."
                bat 'wsl docker push yentanmayi/movie-app:latest'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                bat 'wsl kubectl apply -f k8s/deployment.yaml'
                bat 'wsl kubectl apply -f k8s/service.yaml'
                bat 'wsl kubectl rollout restart deployment/movie-app'
            }
        }
    }
    post {
        success {
            echo 'CI/CD Pipeline Completed Successfully! The app is live on Kubernetes.'
        }
        failure {
            echo 'Pipeline Failed. Check the logs for details.'
        }
    }
}
