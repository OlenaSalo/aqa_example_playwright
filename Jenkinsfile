pipeline {
   agent any
   stages {
      stage('Checkout repo') {
          steps{
             git(url: 'https://github.com/OlenaSalo/aqa_example_playwright.git', branch: 'main')
             }
          }
      stage('e2e-tests') {
//          agent { docker { image 'mcr.microsoft.com/playwright/python:v1.35.0-jammy' } }
         steps {
            sh 'pip3 install -r requirements.txt'
            sh 'pytest'
         allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure_results']]
                    ])
                    }
      }
      stage('Test Docker Connectivity') {
        steps {
             sh 'docker info'
            }
        }
   }
}