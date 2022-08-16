pipeline {
    agent any

    stages {
        stage(‘Build’) {
            sh ‘docker-compose –f build-compose.yml run –rm compile’
        }
    }
}
