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

    private var listOfStrings = new List<string>();

    public partial class App : Application
    {
        private void Application_Startup(object sender, StartupEventArgs e)
        {
            if (e.Args.Length == 1)
                MessageBox.Show("Now opening file: \n\n" + e.Args[0]);
        }
    }
}
