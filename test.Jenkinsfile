pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                build job: 'test/main', parameters: [
                    stashedFile(name: 'HTML', file: [$class: "FileParameterValue", name: "propertiesFile", file: new FileParameterValue.FileItemImpl(new File('test.html'))]),
                    string(name: 'TITLE', value: 'sample of title value')
                ]
            }
        }
    }
}