using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TestStack.White;
using TestStack.White.Factory;
using TestStack.White.ScreenObjects.Services;
using TestStack.White.ScreenObjects.Sessions;
using TestStack.White.UIItems;
using TestStack.White.UIItems.Finders;
using TestStack.White.UIItems.WindowItems;


namespace WhiteLibrary
{
    public class Keywords
    {
        private Application app;
        private Window window;

        public void launch_application(string sut)
        {
            this.app = Application.Launch(sut);
            this.window = app.GetWindow("UI Automation Test Window", InitializeOption.NoCache);
        }

        public void close_application()
        {
            app.Close();
        }

        public void input_text(string locator, string mytext)
        {
            SearchCriteria searchCriteria = SearchCriteria.ByAutomationId(locator);
            TextBox textBox = (TextBox)window.Get(searchCriteria);
            textBox.Text = mytext;
        }      
    }
}