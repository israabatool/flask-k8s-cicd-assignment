// Windows pipeline update
pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app:latest"
        KUBE_NAMESPACE = "default"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    bat "docker build -t %IMAGE_NAME% ."
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo "Applying Kubernetes manifests..."
                    bat "kubectl apply -f kubernetes\\deployment.yaml"
                    bat "kubectl apply -f kubernetes\\service.yaml"
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    echo "Verifying rollout status..."
                    bat "kubectl rollout status deployment/flask-app"
                    bat "kubectl get pods"
                    bat "kubectl get services"
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs!"
        }
    }
}
