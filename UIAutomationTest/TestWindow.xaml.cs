using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace UIAutomationTest
{
    /// <summary>
    /// Interaction logic for TestWindow.xaml
    /// </summary>
    public partial class TestWindow : Window
    {
        public TestWindow()
        {
            InitializeComponent();
        }

        private void calculate_click(object sender, RoutedEventArgs e)
        {
            if (!string.IsNullOrEmpty(txtA.Text) && !string.IsNullOrEmpty(txtB.Text))
            {
                int num1 = int.Parse(txtA.Text);
                int num2 = int.Parse(txtB.Text);
                string opp = (op.SelectedValue as ComboBoxItem).Content.ToString();
                if (opp != "Operator") { tbResult.Text = calculate(num1, opp, num2).ToString(); }
            }
        }

        private int calculate(int num1, string op, int num2)
        {
            switch (Convert.ToChar(op))
            {
                case '+':
                    return num1 + num2;
                case '-':
                    return num1 - num2;
                case '*':
                    return num1 * num2;
                case '/':
                    if (num2 > 0) { return num1 / num2; }
                    else { return 0; }
            }
            return 0;
        }

        private void operator_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {

        }
    }
}
