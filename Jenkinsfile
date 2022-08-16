pipeline{
    agent { dockerfile true }
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