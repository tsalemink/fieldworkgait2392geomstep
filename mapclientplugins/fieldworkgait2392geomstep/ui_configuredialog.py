# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/configuredialog.ui'
#
# Created: Fri Jul 29 16:35:28 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(597, 334)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.configGroupBox = QtGui.QGroupBox(Dialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label0 = QtGui.QLabel(self.configGroupBox)
        self.label0.setObjectName("label0")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label0)
        self.lineEdit_id = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_id)
        self.label = QtGui.QLabel(self.configGroupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_osim_output_dir = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit_osim_output_dir.setObjectName("lineEdit_osim_output_dir")
        self.horizontalLayout.addWidget(self.lineEdit_osim_output_dir)
        self.pushButton_osim_output_dir = QtGui.QPushButton(self.configGroupBox)
        self.pushButton_osim_output_dir.setObjectName("pushButton_osim_output_dir")
        self.horizontalLayout.addWidget(self.pushButton_osim_output_dir)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_2 = QtGui.QLabel(self.configGroupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox_in_unit = QtGui.QComboBox(self.configGroupBox)
        self.comboBox_in_unit.setObjectName("comboBox_in_unit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox_in_unit)
        self.label_4 = QtGui.QLabel(self.configGroupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.comboBox_out_unit = QtGui.QComboBox(self.configGroupBox)
        self.comboBox_out_unit.setObjectName("comboBox_out_unit")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox_out_unit)
        self.label_10 = QtGui.QLabel(self.configGroupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_10)
        self.checkBox_write_osim_file = QtGui.QCheckBox(self.configGroupBox)
        self.checkBox_write_osim_file.setText("")
        self.checkBox_write_osim_file.setObjectName("checkBox_write_osim_file")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.checkBox_write_osim_file)
        self.label_3 = QtGui.QLabel(self.configGroupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_3)
        self.checkBox_scale_other_bodies = QtGui.QCheckBox(self.configGroupBox)
        self.checkBox_scale_other_bodies.setText("")
        self.checkBox_scale_other_bodies.setObjectName("checkBox_scale_other_bodies")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.checkBox_scale_other_bodies)
        self.label_11 = QtGui.QLabel(self.configGroupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_11)
        self.checkBox_GUI = QtGui.QCheckBox(self.configGroupBox)
        self.checkBox_GUI.setEnabled(False)
        self.checkBox_GUI.setText("")
        self.checkBox_GUI.setObjectName("checkBox_GUI")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.checkBox_GUI)
        self.label_5 = QtGui.QLabel(self.configGroupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_subject_mass = QtGui.QLineEdit(self.configGroupBox)
        self.lineEdit_subject_mass.setObjectName("lineEdit_subject_mass")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_subject_mass)
        self.label_6 = QtGui.QLabel(self.configGroupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_6)
        self.checkBox_preserve_mass_dist = QtGui.QCheckBox(self.configGroupBox)
        self.checkBox_preserve_mass_dist.setText("")
        self.checkBox_preserve_mass_dist.setObjectName("checkBox_preserve_mass_dist")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.checkBox_preserve_mass_dist)
        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_id, self.lineEdit_osim_output_dir)
        Dialog.setTabOrder(self.lineEdit_osim_output_dir, self.pushButton_osim_output_dir)
        Dialog.setTabOrder(self.pushButton_osim_output_dir, self.comboBox_in_unit)
        Dialog.setTabOrder(self.comboBox_in_unit, self.comboBox_out_unit)
        Dialog.setTabOrder(self.comboBox_out_unit, self.checkBox_write_osim_file)
        Dialog.setTabOrder(self.checkBox_write_osim_file, self.checkBox_scale_other_bodies)
        Dialog.setTabOrder(self.checkBox_scale_other_bodies, self.checkBox_GUI)
        Dialog.setTabOrder(self.checkBox_GUI, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Configure OpenSim Gait2392 Customisation Step", None, QtGui.QApplication.UnicodeUTF8))
        self.label0.setText(QtGui.QApplication.translate("Dialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Output Directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_osim_output_dir.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Input Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Output Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Output .osim file:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Scale other bodies:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "GUI:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Subject Mass (kg):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Preserve Mass Distribution:", None, QtGui.QApplication.UnicodeUTF8))

