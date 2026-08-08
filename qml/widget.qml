import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import RinUI
import ClassWidgets.Theme
import Qt5Compat.GraphicalEffects

Widget {
    id: root
    text: qsTr("Welcome")
    property var title: settings.target_text
    property var entries: AppCentral.scheduleRuntime.nextEntries || []
    property var subjects: AppCentral.scheduleRuntime.subjects || []
    property int entriesLength: {
        if (entries.length !== 0 && settings.max_length !== null) {
            return entries.length < settings.max_length ? entries.length : settings.max_length
        } else {
            return 0
        }
    }

    MarqueeTitle {
        visible: settings && settings.marquee
        anchors.centerIn: parent
        width: 275
        text: root.title
    }

    Title {
        width: !settings || !settings.marquee ? implicitWidth : 0
        visible: !settings || !settings.marquee
        anchors.centerIn: parent
        text: root.title
    }
}