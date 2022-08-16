pipeline{
    agent any
    stages {
        stage('run docker compose')
            {
            steps{
                echo "============ start building image ============"
                sh 'docker build ./Dockerfile'
            }
        }
    }
}