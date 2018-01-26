using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TestStack.White;
using TestStack.White.UIItems;
using TestStack.White.UIItems.Finders;
using TestStack.White.UIItems.WindowItems;
using TestStack.White.UIItems.ListBoxItems;
using TestStack.White.UIItems.MenuItems;
using TestStack.White.Configuration;
using Castle.Core.Logging;
using System.Reflection;

namespace WhiteLibrary
{
    public class WhiteFW
    {
        protected Window window;

        private Dictionary<string, string> strategies = new Dictionary<string, string>
        {
            {"id", "ByAutomationId"},
            {"text", "ByText"},
            {"index", "AndByIndex"},
        };

        protected void set_logging(string level)
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

        protected TextBox getTextBox(string locator)
        {
            return getItemByLocator<TextBox>(locator);
        }

        protected Slider getSlider(string locator)
        {
            return getItemByLocator<Slider>(locator);
        }

        protected Label getLabel(string locator)
        {
            return getItemByLocator<Label>(locator);
        }

        protected ComboBox getComboBox(string locator)
        {
            return getItemByLocator<ComboBox>(locator);
        }

        protected Button getButton(string locator)
        {
            return getItemByLocator<Button>(locator);
        }

        protected RadioButton getRadioButton(string locator)
        {
            return getItemByLocator<RadioButton>(locator);
        }

        protected CheckBox getCheckBox(string locator)
        {
            return getItemByLocator<CheckBox>(locator);
        }

        protected GroupBox getGroupBox(string locator)
        {
            return getItemByLocator<GroupBox>(locator);
        }

        protected Menu getMenu(string locator)
        {
            return getItemByLocator<Menu>(locator);
        }

        protected ListBox getListBox(string locator)
        {
            return getItemByLocator<ListBox>(locator);
        }

        protected ListItem getListItem(string locator)
        {
            return getItemByLocator<ListItem>(locator);
        }

        protected ProgressBar getProgressBar(string locator)
        {
            return getItemByLocator<ProgressBar>(locator);
        }

        private T getItemByLocator<T>(string locator) where T : IUIItem
        {
            var locatorParts = getLocatorParts(locator);
            string searchStrategy = locatorParts[0];
            string locatorValue = locatorParts[1];

            if (searchStrategy == "partial_text")
            {
                return getItemByPartialText<T>(locatorValue);
            }

            return getItemBySearchCriteria<T>(searchStrategy, locatorValue);
        }

        private string[] getLocatorParts(string locator)
        {
            if (!locator.Contains("="))
            {
                // use automation id as default search strategy if no strategy is defined
                locator = "id=" + locator;
            }
            return locator.Split('=');
        }

        private T getItemByPartialText<T>(string partialText) where T : IUIItem
        {
            IUIItem[] items = window.GetMultiple(SearchCriteria.All);
            return (T)items.First(x => x.GetType() == typeof(T) && x.Name.Contains(partialText));
        }

        private T getItemBySearchCriteria<T>(string searchStrategy, string locatorValue) where T : IUIItem
        {
            SearchCriteria searchCriteria = getSearchCriteria(searchStrategy, locatorValue);
            return window.Get<T>(searchCriteria);
        }
        private SearchCriteria getSearchCriteria(string searchStrategy, string locatorValue)
        {
            string methodName;
            strategies.TryGetValue(searchStrategy, out methodName);
            MethodInfo searchMethod = typeof(SearchCriteria).GetMethod(methodName);
            var methodParameters = new string[] { locatorValue };
            return (SearchCriteria)searchMethod.Invoke(null, methodParameters);
        }
    }
}
