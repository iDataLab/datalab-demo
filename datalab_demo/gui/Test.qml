import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11

StackView {
    id: stack
    initialItem: view

    Component {
        id: view

        MouseArea {
            Text {
                text: stack.depth
                anchors.centerIn: parent
            }
            onClicked: stack.push(view)
        }
    }
}
