pipeline {
  environment {
    imagename = "geniass123/geaniass"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {

  stage('Lint and Test')
        {
        agent { dockerfile true }
            steps
            {
                sh 'black .'
                sh 'flake8 . '
            }

        }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script

        {
          docker.withRegistry( '', registryCredential )
          {
            dockerImage.push()
             dockerImage.push('latest')
          }
        }
      }
    }
  }
}