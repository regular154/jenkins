pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                stash includes: 'test.html', name: 'HTML'
                unstash 'HTML'
                build job: 'test/main', parameters: [
                    stashedFile(name: 'HTML', file: new FileParameterValue("myFile.any", HTML, "myFile.any")),
                    string(name: 'TITLE', value: 'sample of title value')
                ]
            }
        }
    }
}