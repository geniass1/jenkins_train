pipeline
{
    environment
    {
        imagename = "geniass123/jenkins_train"
        registryCredential = 'geniass123-docker-hub'
        dockerImage = ''
    }

agent {dockerfile true}

 stages
 {

 stage('Lint and Test')
        {
        agent { dockerfile true }
            steps
            {
                sh 'black .'
                sh 'flake8 . '
                sh 'pytest'
            }

        }

    stage('Building image')
    {
      steps
      {
        script
        {
          dockerImage = docker.build imagename
        }
      }
    }

    stage('Deploy Image')
    {
      steps
      {
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