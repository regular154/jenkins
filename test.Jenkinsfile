pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'echo $HOME'
                    sh 'ls'
                    sh 'cat $HOME/test.html'
                    writeFile(file: 'HTML', text: readFile(file: 'test.html'))
                    build job: 'test/main', parameters: [
                        stashedFile(name: 'HTML', file: new FileParameterValue("HTML", HTML)),
                        string(name: 'TITLE', value: 'PMDAPI')
                    ]
                }
            }
        }
    }
}