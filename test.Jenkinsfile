pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    stash includes: '/test.html', name: 'HTML'
                    unstash 'HTML'
//                     writeFile(file: 'HTML', text: readFile(file: 'test.html'))
                    build job: 'test/main', parameters: [
                        stashedFile(name: 'HTML', file: new FileParameterValue("HTML", HTML, "HTML")),
                        string(name: 'TITLE', value: 'PMDAPI')
                    ]
                }
            }
        }
    }
}