pipeline {
  agent any
  environment {
    TEST_BASE_URL = credentials('TEST_BASE_URL')
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Setup') {
      steps {
        sh 'python -m pip install --upgrade pip'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Run Smoke') {
      steps {
        sh 'pytest tests/smoke/test_ui_smoke.py -q --maxfail=1'
      }
    }
  }
  post {
    always {
      archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
      junit allowEmptyResults: true, testResults: 'reports/**/*.xml'
    }
  }
}
