pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                script {
                    encodedTestFile = sh(script: 'base64 -w0 test.html', returnStdout: true)
                    build job: 'test/main', parameters: [
                        stashedFile(name: 'HTML', file: encodedTestFile),
                        string(name: 'TITLE', value: 'sample of title value')
                    ]
                }
            }
        }
    }
}