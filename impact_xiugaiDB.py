# Do not edit this file or it may not load correctly
# if you try to open it with the RSG Dialog Builder.

# Note: thisDir is defined by the Activator class when
#       this file gets exec'd

from rsg.rsgGui import *
from abaqusConstants import INTEGER, FLOAT
dialogBox = RsgDialog(title='Laminates Builder', kernelModule='Lamin', kernelFunction='Test', includeApplyBtn=False, includeSeparator=True, okBtnText='OK', applyBtnText='Apply', execDir=thisDir)
RsgTabBook(name='TabBook_1', p='DialogBox', layout='0')
RsgTabItem(name='TabItem_4', p='TabBook_1', text='Geometry')
RsgLabel(p='TabItem_4', text='Default Unit(mm)', useBoldFont=False)
RsgSeparator(p='TabItem_4')
RsgVerticalFrame(name='VFrame_4', p='TabItem_4', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgHorizontalFrame(name='HFrame_2', p='VFrame_4', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgIcon(p='HFrame_2', fileName=r'Geometry.png')
RsgVerticalFrame(name='VFrame_3', p='HFrame_2', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_1', p='VFrame_3', text='Whole', layout='0')
RsgTextField(p='GroupBox_1', fieldType='Float', ncols=12, labelText='Long       ', keyword='Long_Whole', default='170')
RsgTextField(p='GroupBox_1', fieldType='Float', ncols=12, labelText='Width      ', keyword='Width_Whole', default='90')
RsgTextField(p='GroupBox_1', fieldType='Float', ncols=12, labelText='Mesh size', keyword='Mesh_Size_Whole', default='1.2')
RsgGroupBox(name='GroupBox_3', p='VFrame_3', text='Center Area', layout='0')
RsgTextField(p='GroupBox_3', fieldType='Float', ncols=12, labelText='Long       ', keyword='Long_Center', default='40')
RsgTextField(p='GroupBox_3', fieldType='Float', ncols=12, labelText='Width      ', keyword='Width_Center', default='40')
RsgTextField(p='GroupBox_3', fieldType='Float', ncols=12, labelText='Mesh Size', keyword='Mesh_Size_Center', default='0.3')
RsgSeparator(p='VFrame_4')
RsgHorizontalFrame(name='HFrame_3', p='VFrame_4', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgIcon(p='HFrame_3', fileName=r'Impact.png')
RsgVerticalFrame(name='VFrame_5', p='HFrame_3', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_4', p='VFrame_5', text='Impact Head', layout='0')
RsgTextField(p='GroupBox_4', fieldType='Float', ncols=12, labelText='Radius          ', keyword='Radius', default='6.5')
RsgTextField(p='GroupBox_4', fieldType='Float', ncols=12, labelText='Speed(mm/s)', keyword='Speed', default='3200')
RsgTextField(p='GroupBox_4', fieldType='Float', ncols=12, labelText='Mesh Size     ', keyword='Mesh_Size_Impact', default='1')
RsgTabItem(name='TabItem_1', p='TabBook_1', text='Assign')
RsgHorizontalFrame(name='HFrame_18', p='TabItem_1', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgIcon(p='HFrame_18', fileName=r'rotation.png')
RsgIcon(p='HFrame_18', fileName=r'Stack.png')
RsgHorizontalFrame(name='HFrame_19', p='TabItem_1', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgComboBox(name='ComboBox_1', p='HFrame_19', text='Metal:', keyword='Metal_name', default='', comboType='STANDARD', repository='', rootText='', rootKeyword='None', layout='')
RsgComboBox(name='ComboBox_2', p='HFrame_19', text='Polymer:', keyword='polymer_name', default='', comboType='STANDARD', repository='', rootText='', rootKeyword='None', layout='')
materials = mdb.models['Model-1'].materials.keys()
for material in materials:
    RsgListItem(p='ComboBox_1', text=material)
for material in materials:
    RsgListItem(p='ComboBox_2', text=material)
RsgTable(p='TabItem_1', numRows=10, columnData=[('Metal', 'Bool', 100), ('FRP', 'Bool', 100), ('Thickness(mm)', 'Float', 120), ('Rotation Angle( FRP Only )', 'Float', 100)], showRowNumbers=True, showGrids=True, keyword='Stack', popupFlags='AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS')
RsgGroupBox(name='GroupBox_13', p='TabItem_1', text='Attention', layout='LAYOUT_FILL_X')
RsgLabel(p='GroupBox_13', text='Metal or FRP can only be chosen one', useBoldFont=True)
RsgLabel(p='GroupBox_13', text='There must be two layers at least', useBoldFont=True)
RsgTabItem(name='TabItem_2', p='TabBook_1', text='Other')
RsgTextField(p='TabItem_2', fieldType='Float', ncols=12, labelText='Friction Coefficient', keyword='Friction_Coef', default='0.3')
RsgTextField(p='TabItem_2', fieldType='Float', ncols=12, labelText='Total time(s)', keyword='Total_Time', default='0.01')
RsgTextField(p='TabItem_2', fieldType='Integer', ncols=12, labelText='Number of solution-dependent state variables', keyword='SDVn', default='15')
RsgTextField(p='TabItem_2', fieldType='Integer', ncols=12, labelText='Variable number controlling element deletion', keyword='SDVd', default='15')
dialogBox.show()