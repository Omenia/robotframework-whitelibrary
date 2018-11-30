from librarycomponent import LibraryComponent
from robotlibcore import keyword
from TestStack.White import Application


class ApplicationKeywords(LibraryComponent):
    @keyword
    def launch_application(self, sut_path):
        self.state.app = Application.Launch(sut_path)

    @keyword
    def attach_application_by_name(self, sut_name):
        """ Attaches to a running application by name.
        Parameters
        ---------- 
        sut_name: string
            Application process name
        """
        self.state.app = Application.Attach(sut_name)

    @keyword
    def attach_application_by_id(self, sut_id):
        """ Attaches to a running application by id.
        Parameters
        ---------- 
        sut_id: int
            Application process id
        """
        self.state.app = Application.Attach(sut_id)

    @keyword
    def close_application(self):
        """
        Close application
        | No arguments |
        """
        self.state.app.Close()
        self.state.app = None
        self.state.window = None
