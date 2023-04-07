pipeline {
    agent any
    stages {
        stage('trigger job') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'echo $HOME'
                    sh 'ls'
                    sh 'cat $HOME/test.html'
                    build job: 'test/main', parameters: [
                        stashedFile(name: 'HTML', file: getFileItem()),
                        string(name: 'TITLE', value: 'PMDAPI')
                    ]
                }
            }
        }
    }
}

def getFileItem() {
    def myFileContent = readFile("test.html")
    FilePath fp = new FilePath(new File("${WORKSPACE}","HTML"))
    if(fp!=null){
        fp.write(myFileContent, null)
    }
    def file = new File("${WORKSPACE}/HTML")
    return file
}
