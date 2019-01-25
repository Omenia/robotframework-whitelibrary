using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Windows;

namespace UIAutomationTest
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    
    public partial class App : Application
    {
        public static string[] Args;
        void Application_Startup(object sender, StartupEventArgs e)
        {
            // If no command line arguments were provided, don't process them if (e.Args.Length == 0) return;  
            if (e.Args.Length > 0)
            {
                Args = e.Args;
            }
            else
            {
                string[] noArgs = new string[] { "No command line args provided" };
                Args = noArgs;
            }
        }
    }
}