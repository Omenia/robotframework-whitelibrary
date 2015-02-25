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
using TestStack.White.UIItems.ListBoxItems;
using TestStack.White.UIItems.Finders;
using TestStack.White.UIItems.WindowItems;


namespace WhiteLibrary
{
    public class Keywords : WhiteFW
    {
        private Application app;

        public void launch_application(string sut)
        {
            this.app = Application.Launch(sut);
        }

        public void attach_window(string window)
        {
            this.window = app.GetWindow(window, InitializeOption.NoCache);
        }

        public void set_log_level(string level)
        {
            set_logging(level);
        }

        public void close_application()
        {
            app.Close();
        }

        public void input_text_textbox(string locator, string mytext)
        {
            TextBox textBox = getTextBox(locator);
            textBox.Text = mytext;
        }

        public string verify_text_textbox(string locator)
        {
            TextBox textBox = getTextBox(locator);
            return textBox.Text;
        }

        public string verify_label(string locator)
        {
            Label label = getLabel(locator);
            return label.Text;
        }

        public void select_combobox_value(string locator, string value)
        {
            ComboBox comboBox = getComboBox(locator);
            comboBox.Select(value);
        }

        public void select_combobox_index(string locator, int index)
        {
            ComboBox comboBox = getComboBox(locator);
            comboBox.Select(index);
        }

        public string verify_combobox_item(string locator)
        {
            ComboBox comboBox = getComboBox(locator);
            return comboBox.EditableText;
        }

        public string verify_button(string locator)
        {
            Button button = getButton(locator);
            return button.Text;
        }

        public void click_button(string locator)
        {
            Button button = getButton(locator);
            button.Click();
        }
    }
}