pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                script {
                    encodedTestFile = sh(script: 'base64 -w0 test.html', returnStdout: true)
                    build job: 'test/main', parameters: [
                        base64File(name: 'HTML64', value: encodedTestFile)
                        string(name: 'TITLE', value: 'from trigger')
                    ]
                }
            }
        }
    }
}