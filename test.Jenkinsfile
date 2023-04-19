pipeline {
    agent any
    stages {
        stage('Publish GraphQL') {
            steps {
                script {
                    encodedTestFile = sh(script: 'base64 -w0 test.html', returnStdout: true)
                    build job: 'test/main', parameters: [
                        string(name: 'TITLE', value: 'PMDAPI'),
                        base64File(name: 'HTML64', base64: encodedTestFile)
                    ]
                }
            }
        }
    }
}