pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                script {
                    build job: 'test/main', parameters: [
                        string(name: 'TITLE', value: 'title example'),
                        file(name: 'HTML', file: 'test.html')
                ]
            }
        }
    }
}
