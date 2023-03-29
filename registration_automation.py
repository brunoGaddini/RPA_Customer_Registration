import pandas as pd
import robot

excel_file = pd.read_excel('cadastro_clientes.xlsx')
robot.cadastro_web(excel_file)