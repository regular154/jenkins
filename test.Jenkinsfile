pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                build job: 'test/main', parameters: [
                        RESTList(name: 'TITLE', value: 'title example')
                ]
            }
        }
    }
}
