pipeline {
  agent any

  stages {
    stage('Install Pip') {
      steps {
        echo "install curl"
        powershell 'Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py'  // Download get-pip.py
        echo "get py"
        powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\python.exe get-pip.py'  // Replace with the correct path to your Python executable
      }
    }

    stage('Build and Test') {
      steps {
        echo "0.."
        powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\pip install -r requirements.txt'  // Install Python dependencies using PowerShell with full path to pip executable
        echo "1.."
        //  powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\coverage run --source=. -m pytest --verbose test/'  // Run tests with code coverage using PowerShell with full path to coverage executable
        echo "2.."
      }
    }

    stage('Fetch User Data') {
      steps {
        script {
          def downloadDir = "${env.WORKSPACE}"
          echo "Download Directory: ${downloadDir}"
          powershell "cd ${downloadDir}"
          powershell "curl -o user_data.xlsx https://reqres.in/api/users"
          bat "dir ${downloadDir}"
        }
      }
    }

    stage('Generate Excel File') {
      steps {
        powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\python.exe generate_excel.py'  // Run the Python script to generate the Excel file using PowerShell with full path to Python executable
        echo "Contents of workspace directory after generating Excel file:"
        bat 'dir'
      }
      post {
        always {
          archiveArtifacts artifacts: 'user_data.xlsx', onlyIfSuccessful: true  // Archive the Excel file as an artifact
        }
      }
    }

    stage('Coverage Report') {
      steps {
        powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\coverage report -m'  // Generate coverage report using PowerShell with full path to coverage executable
        powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\coverage xml -o coverage.xml'  // Generate coverage report in XML format using PowerShell with full path to coverage executable
      }
    }
  }
}
