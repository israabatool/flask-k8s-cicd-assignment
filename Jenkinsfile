
// Windows pipeline update test
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
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo "Applying Kubernetes manifests..."
                    sh "kubectl apply -f kubernetes/deployment.yaml"
                    sh "kubectl apply -f kubernetes/service.yaml"
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    echo "Verifying rollout status..."
                    sh "kubectl rollout status deployment/flask-app"
                    sh "kubectl get pods"
                    sh "kubectl get services"
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
