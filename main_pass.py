#Author : Eliel Gonzalez
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PasswordG import *
from Password_function import *




class Pass_Generator(QtWidgets.QWidget,Ui_Form):

	def generar_password(self):
		long = int(self.lbl_vis.text())

		# completo

		if self.cb_mayus.isChecked() and self.cb_minus.isChecked() and self.cb_numeros.isChecked() and self.cb_simbolos.isChecked() :
			password = generador_completo(long)

			self.ln_pass.setText(password)

		#--------  3 check box ---------#

		elif self.cb_mayus.isChecked() and self.cb_minus.isChecked() and self.cb_numeros.isChecked():
			password = generador_mayus_minus_numeros(long)

			self.ln_pass.setText(password)

		elif self.cb_mayus.isChecked() and self.cb_numeros.isChecked() and self.cb_simbolos.isChecked() :
			password = generador_mayus_numeros_simb(long)

			self.ln_pass.setText(password)

		elif self.cb_mayus.isChecked() and self.cb_minus.isChecked() and self.cb_simbolos.isChecked() :
			password = generador_mayus_minus_simb(long)

			self.ln_pass.setText(password)

		elif self.cb_minus.isChecked() and self.cb_numeros.isChecked() and self.cb_simbolos.isChecked() :
			password = generador_minus_numeros_simb(long)

			self.ln_pass.setText(password)


		#--------  2 check box ---------#

		elif self.cb_mayus.isChecked() and self.cb_minus.isChecked():
			password = generador_mayus_minus(long)

			self.ln_pass.setText(password)

		elif self.cb_mayus.isChecked() and self.cb_numeros.isChecked():
			password = generador_mayus_num(long)

			self.ln_pass.setText(password)

		elif self.cb_mayus.isChecked() and self.cb_simbolos.isChecked():
			password = generador_mayus_simb(long)

			self.ln_pass.setText(password)

		elif self.cb_minus.isChecked() and self.cb_numeros.isChecked():
			password = generador_minus_num(long)

			self.ln_pass.setText(password)

		elif self.cb_numeros.isChecked() and self.cb_simbolos.isChecked():
			password = generador_num_simb(long)

			self.ln_pass.setText(password)

		elif self.cb_minus.isChecked() and self.cb_simbolos.isChecked():
			password = generador_minus_simb(long)

			self.ln_pass.setText(password)


		#-------- 1 check box ---------#

		elif self.cb_mayus.isChecked():
			password = generador_mayus(long)

			self.ln_pass.setText(password)

		elif self.cb_minus.isChecked():
			password = generador_minus(long)

			self.ln_pass.setText(password)

		elif self.cb_numeros.isChecked():
			password = generador_numeros(long)

			self.ln_pass.setText(password)

		elif self.cb_simbolos.isChecked():
			password = generador_simbolos(long)

			self.ln_pass.setText(password)




	def __init__(self):
		super(Pass_Generator,self).__init__()
		self.setupUi(self)

		self.btn_generar.clicked.connect(self.generar_password)




def main():
	app = QApplication(sys.argv)
	mi_app = Pass_Generator()
	mi_app.show()
	sys.exit(app.exec_())





if __name__ == "__main__":
	main()
