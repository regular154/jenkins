pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                build job: 'test/main', parameters: [
                    file(name: 'HTML', value: '@$HOME/test.html')
                ]
            }
        }
    }
}
