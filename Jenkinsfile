pipeline {
    agent any
    environment{
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }
    stages{
        stage('gitclone'){
            steps{
                git 'https://github.com/geniass1/jenkins_train.git'
            }
        }
        stage('Build'){
            steps {
                sh 'docker build -t geniass123/jenkins_train .'
            }
        }
        stage('Login'){
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
    }


}