pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                build job: 'test/main', parameters: [
                        string(name: 'TITLE', value: 'title example'),
                        stashedFile(name: 'HTML', file: 'test.html')
                ]
            }
        }
    }
}
