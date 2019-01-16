using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
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
        private int doubleClickCounter = 0;
        private int initialProgress = 4;
        public TestWindow()
        {
            InitializeComponent();
        }

        private void calculate_click(object sender, RoutedEventArgs e)
        {
            if (!string.IsNullOrEmpty(txtA.Text) && !string.IsNullOrEmpty(txtB.Text))
            {
                try
                {
                    double num1 = double.Parse(txtA.Text);
                    double num2 = double.Parse(txtB.Text);
                    string opp = (op.SelectedValue as ComboBoxItem).Content.ToString();
                    tbResult.Text = calculate(num1, opp, num2).ToString();
                }
                catch (FormatException) { }
            }
        }

        private double calculate(double num1, string op, double num2)
        {
            switch (Convert.ToChar(op))
            {
                case '+':
                    return num1 + num2;
                case '-':
                    return num1 - num2;
                case '*':
                    return num1 * num2;
                case '%':
                    return num1 % num2;
                case '/':
                    if (num2 > 0) { return num1 / num2; }
                    else { return 0; }
            }
            return 0;
        }

        private void progressClick(object sender, RoutedEventArgs e)
        {
            double newVal = proggis.Value + 20;
            if (newVal > 100) { newVal = this.initialProgress; }
            proggis.Value = newVal;
        }

        private void progressReset(object sender, RoutedEventArgs e)
        {
            proggis.Value = this.initialProgress;
        }

        private void changeName(object sender, RoutedEventArgs e)
        {
            MenuItem mi = sender as MenuItem;
            ContextMenu cm = mi.CommandParameter as ContextMenu;
            ListBox lb = cm.PlacementTarget as ListBox;
            ListBoxItem item = lb.SelectedItem as ListBoxItem;
            MessageBox.Show("Not implemented yet.\nWhat's wrong with " + item.Content.ToString() +" anyway?");
        }

        private void doubleClickLabel(object sender, RoutedEventArgs e)
        {
            Label lab = sender as Label;
            lab.Content = "Double-clicked " + ++this.doubleClickCounter + " times";
        }

        private void menuAboutClick(object sender, RoutedEventArgs e)
        {
            string text = "This is basic calculator application for testing white library";
            string title = "About";
            MessageBoxButton button = MessageBoxButton.OK;
            MessageBox.Show(text, title, button);
        }

        private void treeNodeSelect(object sender, RoutedEventArgs e)
        {
            treeNodeEvent(sender, e, "selected");
        }

        private void treeNodeDoubleClick(object sender, RoutedEventArgs e)
        {
            treeNodeEvent(sender, e, "double-clicked");
        }

        private void treeNodeRightClick(object sender, RoutedEventArgs e)
        {
            treeNodeEvent(sender, e, "right-clicked");
        }

        private void treeNodeExpanded(object sender, RoutedEventArgs e)
        {
            treeNodeEvent(sender, e, "expanded");
        }

        private void treeNodeEvent(object sender, RoutedEventArgs e, string message)
        {
            TreeViewItem node = sender as TreeViewItem;
            if (node != null)
            {
                selectionIndicatorLabel.Content = node.Header + " " + message;
            }
            e.Handled = true;

        }

        private void toolStripButtonClick(object sender, RoutedEventArgs e)
        {            
            toolStripButtonEvent(sender, e, "clicked");
        }

        private void toolStripButtonEvent(object sender, RoutedEventArgs e, string message)
        {
            if (sender != null)
            {
                Button node = sender as Button;
                selectionIndicatorLabel.Content = node.Content + " " + message;
            }
            e.Handled = true;

        }
        
        private void dataGridCellSelect(object sender, RoutedEventArgs e)
        {
            dataGridCellEvent(sender, e, "selected");
        }

        private void dataGridCellRightClick(object sender, RoutedEventArgs e)
        {
            dataGridCellEvent(sender, e, "right clicked");
        }

        private void dataGridCellDoubleClick(object sender, RoutedEventArgs e)
        {
            dataGridCellEvent(sender, e, "double clicked");
        }

        private void dataGridCellEvent(object sender, RoutedEventArgs e, string message)
        {
            
            DataGridCell node = sender as DataGridCell;
            TextBlock cellText = node.Content as TextBlock;
            if (node != null)
            {
                selectionIndicatorLabel.Content = cellText.Text + " " + message;
            }
            e.Handled = true;

        }

        private async void alertFast(object sender, RoutedEventArgs e)
        {
            await TaskEx.Delay(1000);
            selectionIndicatorLabel.Content = "Fast alert occurred";
        }

        private async void alertSlow(object sender, RoutedEventArgs e)
        {
            await TaskEx.Delay(5000);
            selectionIndicatorLabel.Content = "Slow alert occurred";
        }


    }
}
