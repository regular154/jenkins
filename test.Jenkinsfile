pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                stash includes: 'test.html', name: 'HTML'
                build(job: 'test/main', parameters: [stashedFile(name: 'HTML', file: 'HTML')])

//                 script {
//                     encodedTestFile = sh(script: 'base64 -w0 test.html', returnStdout: true)
//                     stash includes: 'dist/**/*', name: 'builtSources'
//                     build job: 'test/main', parameters: [
//                         stashedFile(name: 'HTML'),
//                         string(name: 'TITLE', value: 'from trigger')
//                     ]
//                 }
            }
        }
    }
}