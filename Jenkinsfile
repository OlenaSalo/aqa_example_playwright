pipeline {
   agent any

   stages {
      stage('Checkout repo') {
          steps{
             git(url: 'https://github.com/OlenaSalo/aqa_example_playwright.git', branch: 'main')
             }
          }
      stage('e2e-tests') {
         agent { docker { image 'mcr.microsoft.com/playwright/python:v1.35.0-jammy' } }
         steps {
            sh 'pip install -r requirements.txt'
            sh 'pytest'
         }
      }
   }
}