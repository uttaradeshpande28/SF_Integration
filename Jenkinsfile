pipeline {
  agent any

  stages {
    stage('Install Pip') {
      steps {
        echo "install curl"
        powershell 'Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py'  // Download get-pip.py
        echo "get py"
        powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\python.exe get-pip.py'  // Replace with the correct path to your Python executable
        #echo "install"
        #powershell 'pip install -r requirements.txt'  // Install Python dependencies using PowerShell
      }
    }

    stage('Build and Test') {
      steps {
        echo "0.."
        powershell 'pip install -r requirements.txt'  // Install Python dependencies using PowerShell
        echo "1.."
        powershell 'coverage run --source=your_source_directory -m pytest tests/'  // Run tests with code coverage using PowerShell
        echo "2.."
      }
    }

    stage('Fetch User Data') {
      steps {
        powershell 'curl -o user_data.xlsx https://reqres.in/api/users'  // Example shell command using PowerShell
      }
    }

    stage('Generate Excel File') {
      steps {
        powershell 'python generate_excel.py'  // Run the Python script to generate the Excel file using PowerShell
      }
      post {
        always {
          archiveArtifacts artifacts: 'user_data.xlsx', onlyIfSuccessful: true  // Archive the Excel file as an artifact
        }
      }
    }

    stage('Coverage Report') {
      steps {
        powershell 'coverage report -m'  // Generate coverage report using PowerShell
        powershell 'coverage xml -o coverage.xml'  // Generate coverage report in XML format using PowerShell
      }
    }
  }
}
