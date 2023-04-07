pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    build job: 'test/main', parameters: [
                        stashedFile(name: 'HTML', file: new FileParameterValue("HTML", HTML, "HTML")),
                        string(name: 'TITLE', value: 'PMDAPI')
                    ]
                }
            }
        }
    }
}