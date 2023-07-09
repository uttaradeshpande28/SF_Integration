pipeline {
  agent any
  
  stages {
    stage('Clear Workspace') {
      steps {
        cleanWs()
      }
    }
      
    stage('Install Pip') {
      steps {
        echo "install curl"
        powershell 'Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py'  // Download get-pip.py
        echo "get py"
        powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\python.exe get-pip.py'  // Replace with the correct path to your Python executable
      }
    }

    stage('Fetch Requirements File') {
      steps {
        script {
          def downloadDir = "${env.WORKSPACE}"
          def branch = "feature/sf"  // Replace with the desired branch name
          def fileURL = "https://raw.githubusercontent.com/uttaradeshpande28/SF_Integration/${branch}/requirements.txt"
    
          echo "Download Directory: ${downloadDir}"
    
          powershell "Invoke-WebRequest -Uri ${fileURL} -OutFile ${downloadDir}/requirements.txt"
    
          echo "Requirements file downloaded and saved at: ${downloadDir}/requirements.txt"
        }
      }
    }
  
    stage('Build and Test') {
      steps {
        echo "0.."
        powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\pip install -r requirements.txt'  // Install Python dependencies using PowerShell with the full path to the pip executable
        echo "1.."
        powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\pip install pillow'  // Install Pillow
        echo "2.."
        // powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\coverage run --source=. -m pytest --verbose test/'  // Run tests with code coverage using PowerShell with the full path to the coverage executable
        echo "3.."
      }
    }

    stage('Fetch User Data') {
      steps {
        script {
          def downloadDir = "${env.WORKSPACE}"
          echo "Download Directory: ${downloadDir}"
          powershell "cd ${downloadDir}"
          powershell "curl -o user_data.xls https://reqres.in/api/users"
          bat "dir ${downloadDir}"
        }
      }
    }

    stage('Generate Excel File') {
      steps {
        script {
          def downloadDir = "${env.WORKSPACE}"
          def branch = "feature/sf"  // Replace with the desired branch name
          def fileURL = "https://raw.githubusercontent.com/uttaradeshpande28/SF_Integration/${branch}/generate_excel.py"
    
          echo "Download Directory: ${downloadDir}"
    
          powershell "Invoke-WebRequest -Uri ${fileURL} -OutFile ${downloadDir}/generate_excel.py"
          powershell "C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\python.exe ${downloadDir}/generate_excel.py"  // Run the Python script to generate the Excel file using PowerShell with the full path to the Python executable
    
          echo "Contents of workspace directory after generating Excel file:"
          bat 'dir'
        }
      }
      post {
        always {
          archiveArtifacts artifacts: 'user_data.xls', onlyIfSuccessful: true  // Archive the Excel file as an artifact
        }
      }
    }

    stage('Coverage Report') {
      steps {
        powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\coverage report -m'  // Generate coverage report using PowerShell with the full path to the coverage executable
        powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\coverage xml -o coverage.xml'  // Generate coverage report in XML format using PowerShell with the full path to the coverage executable
      }
      post {
        always {
          archiveArtifacts artifacts: 'coverage.xml', onlyIfSuccessful: true  // Archive the coverage.xml file as an artifact
        }
      }
    }
  }
}
