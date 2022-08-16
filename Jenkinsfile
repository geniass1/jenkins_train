pipeline{
    agent none
    stages {
        stage('run docker compose')
            {
            steps{
                echo "============ start building image ============"
                sh 'docker compose run --build'
            }
        }
    }
}