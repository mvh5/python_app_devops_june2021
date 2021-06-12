pipeline {
  agent any
  stages {
    stage('Inicio_Environment') {
      steps {
        echo 'Iniciando construccion de proyectos'
        sh 'env'
        sh 'export PATH=$PATH:/usr/local/bin/'
      }
    }

    stage('Docker Env') {
      parallel {
        stage('Docker Env') {
          steps {
            sh 'docker -v'
          }
        }

        stage('Images from docker') {
          steps {
            sh 'docker images'
          }
        }

      }
    }

  }
}