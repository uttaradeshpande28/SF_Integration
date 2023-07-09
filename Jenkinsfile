pipeline {
  agent any

  environment {
    downloadDir = "${env.WORKSPACE}"
    branch = "feature/sf"
    url = "https://raw.githubusercontent.com/uttaradeshpande28/SF_Integration/${branch}"
    fileURL = "${url}/generate_pdf.py"
  }
  
  stages {
    stage('Clear Workspace') {
      steps {
        cleanWs()
      }
    }
      
    stage('Installations') {
      steps {
        echo "install curl"
        powershell 'Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py'  // Download get-pip.py
        echo "get py"
        powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\python.exe get-pip.py'  // Replace with the correct path to your Python executable
      }
    }

    stage('pre-build') {
      steps {
        script {
          echo "Download Directory: ${downloadDir}"
          
          // Remove the existing requirements.txt file if it exists
          powershell "Remove-Item -Path '${downloadDir}/requirements.txt' -ErrorAction SilentlyContinue"
          // get requirement.txt
          powershell "Invoke-WebRequest -Uri ${url}/requirements.txt -OutFile ${downloadDir}/requirements.txt"
          echo "Requirements file downloaded and saved at: ${downloadDir}/requirements.txt"
          
          // Install Python dependencies using pip
          powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\pip install -r requirements.txt'  // Install Python dependencies using PowerShell with the full path to the pip executable
          
          // Install the Pillow library for image processing
          powershell 'C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\pip install pillow'  // Install Pillow
        }
      }
    }
  
    stage('test') {
      steps {
        script {
          echo "Download Directory: ${downloadDir}"
          
          // Remove the existing test file if it exists
          powershell "Remove-Item -Path '${downloadDir}/test_generate_pdf.py' -ErrorAction SilentlyContinue"
          // get test_generate_pdf.py
          powershell "Invoke-WebRequest -Uri ${url}/test -OutFile ${downloadDir}/test_generate_pdf.py"
          echo "Test file downloaded and saved at: ${downloadDir}/test_generate_pdf.py"
        }
      }
    }
    
    stage('build') {
      steps {
        script {
          echo "Download Directory: ${downloadDir}"
    
          powershell "Invoke-WebRequest -Uri ${fileURL} -OutFile ${downloadDir}/generate_pdf.py"
          powershell "C:\\Users\\Uttara\\AppData\\Local\\Programs\\Python\\Python38\\python.exe ${downloadDir}/generate_pdf.py"  // Run the Python script to generate the Excel file using PowerShell with the full path to the Python executable
    
          echo "Contents of workspace directory after generating Excel file:"
          bat 'dir'
        }
      }
      post {
        always {
          archiveArtifacts artifacts: 'user_data.pdf', onlyIfSuccessful: true  // Archive the Excel file as an artifact
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
