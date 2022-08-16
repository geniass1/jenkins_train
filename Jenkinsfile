pipeline{
    agent {
    label: 'master'
    }
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