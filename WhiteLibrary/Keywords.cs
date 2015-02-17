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
        ///Application application = Application.Launch("UIAutomationTest.exe");
        ///Window window = application.GetWindow("UI Automation Test Window", InitializeOption.NoCache);

        ///System.Threading.Thread.Sleep(5000);


        public void alkujuttu()
        {
            Application application = Application.Launch("UIAutomationTest.exe");
            Window window = application.GetWindow("UI Automation Test Window", InitializeOption.NoCache);
        }

        public void input_text(string locator, string mytext)
        {
            SearchCriteria searchCriteria = SearchCriteria.ByAutomationId(locator);
            TextBox textBox = (TextBox)window.Get(searchCriteria);
            textBox.Text = mytext;
        }      
    }
}