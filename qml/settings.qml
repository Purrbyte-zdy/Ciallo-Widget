import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import RinUI
import ClassWidgets.Plugins

SettingsLayout {
    SettingCard {
        Layout.fillWidth: true
        title: "Text"
        description: "Target text for the welcome message."


        TextField {
            Layout.fillWidth: true
            id: textField
            text: settings.target_text
            onTextChanged: {
                settings.target_text = text
            }
        }
    }

    SettingCard {
        Layout.fillWidth: true
        title: "Display on class or activity."
        description: "It's not recommended to open this entry, which is likely to cause arguments."

        Switch {
            checked: settings.display_in_class
            onCheckedChanged: {
                settings.display_in_class = checked
            }
        }
    }
}