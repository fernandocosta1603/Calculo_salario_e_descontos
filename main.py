import PySimpleGUI as sg
import win32com.client as win32

layout = [
    [sg.Text('Digite o valor da hora trabalhada: ')],
    [sg.InputText(key='INPUT_SALARIO_HORA')],
    [sg.Text('Digite a quantidade de horas trabalhadas no mês: ')],
    [sg.InputText(key='INPUT_HORAS_TRABALHADAS')],
    [sg.Button('Calcular'), sg.Button('Cancelar')],
    [sg.Text((''), key='OUTPUT_SALARIO_BRUTO')],
    [sg.Text((''), key='OUTPUT_DESC_IRPF')],
    [sg.Text((''), key='OUTPUT_DESC_INSS')],
    [sg.Text((''), key='OUTPUT_DESC_SINDICATO')],
    [sg.Text((''), key='OUTPUT_DESC_FGTS')],
    [sg.Text((''), key='OUTPUT_DESC_TOTAL')],
    [sg.Text((''), key='OUTPUT_SALARIO_LIQUIDO')],
]

janela = sg.Window('Sistema Cálculo Salário', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Calcular':
        salario_hora = valores['INPUT_SALARIO_HORA']
        horas_trabalhadas = valores['INPUT_HORAS_TRABALHADAS']
        salario_bruto = float(salario_hora) * float(horas_trabalhadas)
        desc_sindicato = salario_bruto * 0.03
        desc_inss = salario_bruto * 0.1
        desc_fgts = salario_bruto * 0.11
        if salario_bruto <= 900:
            desc_irpf = 0
        elif salario_bruto > 900 and salario_bruto <= 1500:
            desc_irpf = salario_bruto * 0.05
        elif salario_bruto > 1500 and salario_bruto <= 2500:
            desc_irpf = salario_bruto * 0.1
        else:
            desc_irpf = salario_bruto * 0.2
        if salario_bruto <= 900:
            perc_irpf = 0
        elif salario_bruto > 900 and salario_bruto <= 1500:
            perc_irpf = 5
        elif salario_bruto > 1500 and salario_bruto <= 2500:
            perc_irpf = 10
        else:
            perc_irpf = 20
        total_descontos = desc_irpf + desc_sindicato + desc_inss
        salario_liquido = salario_bruto - total_descontos

        janela["OUTPUT_SALARIO_BRUTO"].update(f'Salário Bruto: R$ {salario_bruto:.2f}')
        janela["OUTPUT_DESC_IRPF"].update(f'(-) IRPF {perc_irpf:%}: R$ {desc_irpf:.2f}')
        janela["OUTPUT_DESC_INSS"].update(f'(-) INSS: R$ {desc_inss:.2f}')
        janela["OUTPUT_DESC_SINDICATO"].update(f'(-) Sindicato R$ {desc_sindicato:.2f}')
        janela["OUTPUT_DESC_FGTS"].update(f'FGTS (11%): R$ {desc_fgts:.2f}')
        janela["OUTPUT_DESC_TOTAL"].update(f'Total descontos: R$ {total_descontos:.2f}')
        janela["OUTPUT_SALARIO_LIQUIDO"].update(f'Salário Líquido: R$ {salario_liquido:.2f}')


janela.close()