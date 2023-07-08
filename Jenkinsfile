pipeline {
  agent any

  stages {
    stage('Build and Test') {
      steps {
        sh 'pip install -r requirements.txt'  // Install Python dependencies
        sh 'coverage run --source=your_source_directory -m pytest tests/'  // Run tests with code coverage
      }
    }

    stage('Fetch User Data') {
      steps {
        script {
          // Make an API call to fetch user data
          def userData = sh(returnStdout: true, script: 'curl https://reqres.in/api/users')
          // Write the API response to a JSON file
          writeFile file: 'user_data.json', text: userData
        }
      }
    }

    stage('Generate Excel File') {
      steps {
        sh 'python generate_excel.py'  // Run the Python script to generate the Excel file
      }
      post {
        always {
          archiveArtifacts artifacts: 'user_data.xlsx', onlyIfSuccessful: true  // Archive the Excel file as an artifact
        }
      }
    }

    stage('Coverage Report') {
      steps {
        sh 'coverage report -m'  // Generate coverage report
        sh 'coverage xml -o coverage.xml'  // Generate coverage report in XML format
      }
    }
  }
}
