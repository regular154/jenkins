pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                encodedTestFile = sh(script: 'base64 -w0 test.html', returnStdout: true)
                build(job: 'test/main', parameters: [
                        string(name: 'TITLE', value: 'title example'),
                        base64File(name: 'HTML64', base64: encodedTestFile)
                    ]
                )
            }
        }
    }
}