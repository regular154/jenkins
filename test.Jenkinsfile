pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                build job: 'test/main', parameters: [
                    stashedFile(name: 'HTML', file: readFile(file: 'test.html'))
                    string(name: 'TITLE', value: 'sample of title value')
                ]
            }
        }
    }
}