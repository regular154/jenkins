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

@NonCPS
def getFileItem() {
    def largeFileObject = new File(pwd(), "test.html")
    def diskFileItem = new org.apache.commons.fileupload.disk.DiskFileItem("fieldNameFile", "application/vnd.android.package-archive", false, largeFileObject.getName(), (int) largeFileObject.length() , largeFileObject.getParentFile())
    def inputStream = new FileInputStream(largeFileObject)
    def outputStream = diskFileItem.getOutputStream()
    org.apache.commons.io.IOUtils.copy(inputStream, outputStream)
    inputStream.close()
    outputStream.close()
    return diskFileItem
}
