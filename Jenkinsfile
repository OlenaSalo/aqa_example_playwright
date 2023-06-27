pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.35.0-jammy' } }
   stages {
      stage('Checkout repo') {
               git(url: 'https://github.com/OlenaSalo/aqa_example_playwright.git', branch: 'main')
              }
      stage('e2e-tests') {
         steps {
            sh 'pip install -r requirements.txt'
            sh 'pytest'
         }
      }
   }
}