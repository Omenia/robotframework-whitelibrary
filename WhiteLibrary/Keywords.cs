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
using TestStack.White.Configuration;
using Castle.Core.Logging;


namespace WhiteLibrary
{
    public class Keywords
    {
        private Application app;
        private Window window;

        public void launch_application(string sut)
        {
            this.app = Application.Launch(sut);
        }

        public void attach_window(string window)
        {
            this.window = app.GetWindow(window, InitializeOption.NoCache);
        }

        public void close_application()
        {
            app.Close();
        }

        public void set_log_level(string level)
        {
            switch (level.ToLower())
            {
                case "info":
                    CoreAppXmlConfiguration.Instance.LoggerFactory = new WhiteDefaultLoggerFactory(LoggerLevel.Info);
                    break;
                case "warn":
                    CoreAppXmlConfiguration.Instance.LoggerFactory = new WhiteDefaultLoggerFactory(LoggerLevel.Warn);
                    break;
                case "debug":
                    CoreAppXmlConfiguration.Instance.LoggerFactory = new WhiteDefaultLoggerFactory(LoggerLevel.Debug);
                    break;
            }
        }

        public void input_text(string locator, string mytext)
        {
            SearchCriteria searchCriteria = SearchCriteria.ByAutomationId(locator);
            TextBox textBox = (TextBox)window.Get(searchCriteria);
            textBox.Text = mytext;
        }

        public string verify_text(string locator)
        {
            SearchCriteria searchCriteria = SearchCriteria.ByAutomationId(locator);
            TextBox textBox = (TextBox)window.Get(searchCriteria);
            return textBox.Text;
        }
    }
}