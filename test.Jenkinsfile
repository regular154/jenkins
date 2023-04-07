pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'echo $HOME'
                    sh 'ls'
                    sh 'cat $HOME/test.html'
                    defFile()
                    build job: 'test/main', parameters: [
                        stashedFile(name: 'HTML', file: new FileParameterValue("HTML", HTML, "HTML")),
                        string(name: 'TITLE', value: 'PMDAPI')
                    ]
                }
            }
        }
    }
}

def defFile() {
    def myFile = new File("${WORKSPACE}/HTML")
}