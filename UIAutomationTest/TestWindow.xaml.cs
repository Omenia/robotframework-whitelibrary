﻿using System;
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

        }
    }
}
