node {
        stage 'Checkout'
            git url: 'https://github.com/Omenia/robotframework-whitelibrary.git'
        stage 'Build'
            bat 'nuget RobotFrameworkWhiteLibrary.sln'
		    bat 'msbuild RobotFrameworkWhiteLibrary.sln /toolsversion:12.0'
        stage 'Execute tests'
            echo 'Ajan testit whitelle'
        stage 'Publish'
            echo 'Julkaisen'
        stage 'Test'
            echo 'Testi'

}
