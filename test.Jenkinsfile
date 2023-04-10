pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                encodedTestFile = sh(script: 'base64 -w0 test.html', returnStdout: true)
                build job: 'test/main', parameters: [
                    base64File(name: 'HTML', base64: encodedTestFile),
                    string(name: 'TITLE', value: 'sample of title value')
                ]
            }
        }
    }
}