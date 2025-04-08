pipeline {
    agent { label 'small' }
    environment {
      imagename_temp_data_cleaning_dev = "10.3.7.221:5000/temp-data-cleaning"
      imagename_workdir_cleaning_dev = "10.3.7.221:5000/workdir-cleaning"
      imagename_temp_data_cleaning_staging = "10.3.7.241:5000/temp-data-cleaning"
      imagename_workdir_cleaning_staging = "10.3.7.241:5000/workdir-cleaning"
      registryCredential = 'docker-registry'
      dockerImage = ''
    }

    stages {

    stage('Clone sources for k8s-dev') {
        when {branch "k8s-dev"}
        steps{
          script {
          git branch: "k8s-dev",
              url: 'https://git.indocresearch.org/platform/service_scheduled_tasks.git',
              credentialsId: 'lzhao'
            }
        }
    }

    stage('test') {
        when {branch "k8s-dev"}
      steps{
        sh "id"
        sh "pwd"
        sh "hostname"
      }
    }

    stage('DEV Building image temp-data-cleaning') {
      when {
          allOf {
              changeset "temp-data-cleaning/*"
              branch "k8s-dev"
            }
      }
      steps{
        script {
            docker.withRegistry('http://10.3.7.221:5000', registryCredential) {
                customImage = docker.build("10.3.7.221:5000/temp-data-cleaning:${env.BUILD_ID}", "./temp-data-cleaning")
                customImage.push()
            }
        }
      }
    }

    stage('DEV Remove Unused docker image temp-data-cleaning') {
      when {
          allOf {
              changeset "temp-data-cleaning/*"
              branch "k8s-dev"
            }
      }
      steps{
        sh "docker rmi $imagename_temp_data_cleaning_dev:$BUILD_NUMBER"
      }
    }

    stage('DEV Deploy to Kubernetes cluster temp-data-cleaning') {
      when {
          allOf {
              changeset "temp-data-cleaning/*"
              branch "k8s-dev"
            }
      }
      steps{
        sh "sed -i 's/<VERSION>/${BUILD_NUMBER}/g' kubernetes/dev-temp-data-cleaning-deployment.yaml"
        sh "kubectl config use-context dev"
        sh "kubectl apply -f kubernetes/dev-temp-data-cleaning-deployment.yaml"
      }
    }

    stage('DEV Building image workdir-cleaning') {
      when {
          allOf {
              changeset "workdir-cleaning/*"
              branch "k8s-dev"
            }
      }
      steps{
        script {
            docker.withRegistry('http://10.3.7.221:5000', registryCredential) {
                customImage = docker.build("10.3.7.221:5000/workdir-cleaning:${env.BUILD_ID}", "./workdir-cleaning")
                customImage.push()
            }
        }
      }
    }

    stage('DEV Remove Unused docker image workdir-cleaning') {
      when {
          allOf {
              changeset "workdir-cleaning/*"
              branch "k8s-dev"
            }
      }
      steps{
        sh "docker rmi $imagename_workdir_cleaning_dev:$BUILD_NUMBER"
      }
    }

    stage('DEV Deploy to Kubernetes cluster workdir-cleaning') {
      when {
          allOf {
              changeset "workdir-cleaning/*"
              branch "k8s-dev"
            }
      }
      steps{
        sh "sed -i 's/<VERSION>/${BUILD_NUMBER}/g' kubernetes/dev-workdir-cleaning-deployment.yaml"
        sh "kubectl config use-context dev"
        sh "kubectl apply -f kubernetes/dev-workdir-cleaning-deployment.yaml"
      }
    }

    stage('Clone sources for k8s-staging') {
        when {branch "k8s-staging"}
        steps{
          script {
          git branch: "k8s-staging",
              url: 'https://git.indocresearch.org/platform/service_scheduled_tasks.git',
              credentialsId: 'lzhao'
            }
        }
    }

    stage('STAGING Building image temp-data-cleaning') {
      when {
          allOf {
              changeset "temp-data-cleaning/*"
              branch "k8s-staging"
            }
      }
      steps{
        script {
            docker.withRegistry('http://10.3.7.241:5000', registryCredential) {
                customImage = docker.build("10.3.7.241:5000/temp-data-cleaning:${env.BUILD_ID}", "./temp-data-cleaning")
                customImage.push()
            }
        }
      }
    }

    stage('STAGING Remove Unused docker image temp-data-cleaning') {
      when {
          allOf {
              changeset "temp-data-cleaning/*"
              branch "k8s-staging"
            }
      }
      steps{
        sh "docker rmi $imagename_temp_data_cleaning_staging:$BUILD_NUMBER"
      }
    }

    stage('STAGING Deploy to Kubernetes cluster temp-data-cleaning') {
      when {
          allOf {
              changeset "temp-data-cleaning/*"
              branch "k8s-staging"
            }
      }
      steps{
        sh "sed -i 's/<VERSION>/${BUILD_NUMBER}/g' kubernetes/staging-temp-data-cleaning-deployment.yaml"
        sh "kubectl config use-context staging"
        sh "kubectl apply -f kubernetes/staging-temp-data-cleaning-deployment.yaml"
      }
    }

    stage('STAGING Building image workdir-cleaning') {
      when {
          allOf {
              changeset "workdir-cleaning/*"
              branch "k8s-staging"
            }
      }
      steps{
        script {
            docker.withRegistry('http://10.3.7.241:5000', registryCredential) {
                customImage = docker.build("10.3.7.241:5000/workdir-cleaning:${env.BUILD_ID}", "./workdir-cleaning")
                customImage.push()
            }
        }
      }
    }

    stage('STAGING Remove Unused docker image workdir-cleaning') {
      when {
          allOf {
              changeset "workdir-cleaning/*"
              branch "k8s-staging"
            }
      }
      steps{
        sh "docker rmi $imagename_workdir_cleaning_staging:$BUILD_NUMBER"
      }
    }

    stage('STAGING Deploy to Kubernetes cluster workdir-cleaning') {
      when {
          allOf {
              changeset "workdir-cleaning/*"
              branch "k8s-staging"
            }
      }
      steps{
        sh "sed -i 's/<VERSION>/${BUILD_NUMBER}/g' kubernetes/staging-workdir-cleaning-deployment.yaml"
        sh "kubectl config use-context staging"
        sh "kubectl apply -f kubernetes/staging-workdir-cleaning-deployment.yaml"
      }
    }
  }
}
