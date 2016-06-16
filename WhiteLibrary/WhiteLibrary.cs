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
using TestStack.White.UIItems.MenuItems;
using TestStack.White.UIItems.ListBoxItems;
using TestStack.White.UIItems.Finders;
using TestStack.White.UIItems.WindowItems;
using WhiteLibrary;


namespace CSWhiteLibrary
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
            this.window = app.GetWindow(window);
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

        public void set_slider(string locator, Double myvalue)
        {
            Slider myslider = getSlider(locator);
            myslider.Value = myvalue;
        }

        public string verify_text_textbox(string locator)
        {
            TextBox textBox = getTextBox(locator);
            return textBox.Text;
        }
     
        public Double verify_slider(string locator)
        {
            Slider mySlider = getSlider(locator);
            return mySlider.Value;
        }

        public Double verify_progressbar(string locator)
        {
            ProgressBar myProgressBar = getProgressBar(locator);
            return myProgressBar.Value;
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

        public void select_listbox_value(string locator, string value)
        {
            ComboBox listBox = getComboBox(locator);
           // ListItem listItem = getListItem(value);
           // listBox.Select(getListItem(value).ToString());
        }

        public string verify_listbox_value(string locator, string value)
        {
            ListBox listBox = getListBox(locator);
            return listBox.SelectedItemText;
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

        public void select_radio_button(string locator)
        {
            RadioButton radio_button = getRadioButton(locator);
            radio_button.Select();
        }
        
        public Boolean verify_radio_button(string locator)
        {
            RadioButton radio_button = getRadioButton(locator);
            return radio_button.IsSelected;
        }

        public Boolean verify_check_box(string locator)
        {
            CheckBox check_box = getCheckBox(locator);
            return check_box.IsSelected;
        }

        public void toggle_check_box(string locator)
        {
            CheckBox check_box = getCheckBox(locator);
            check_box.Toggle();
        }

        public string verify_menu(string locator)
        {
            Menu menu = getMenu(locator);
            return menu.Name;
        }

        public void click_menu_button(string locator)
        {
            Menu menu = getMenu(locator);
            menu.Click();
        }

        public void select_modal_window(string locator)
        {
            List<Window> modalWindows = window.ModalWindows();
            this.window = window.ModalWindow(locator);
        }
    }
}