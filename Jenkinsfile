pipeline {
  environment {
    imagename = "geniass123/geniass"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {

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