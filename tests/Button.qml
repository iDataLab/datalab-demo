import QtQuick 2.5

Rectangle {
    id: root
    width: 80
    height: 25
    color: "red"
    signal clicked()
    property var text

    Text {
        id: txt
        anchors.fill: parent
        text: root.text
    }

    MouseArea {
        anchors.fill: parent
        onClicked: {
            console.log("Button clicked")
            root.clicked()
        }
    }

}
