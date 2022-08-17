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
      agent {dockerfile true}
        script {
          dockerImage = docker.build dockerfile
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