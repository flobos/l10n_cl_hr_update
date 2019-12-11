"# l10n_cl_hr_update" 



Cambiar Codigo python de regla salarial: 



if worked_days.WORK100.number_of_days > 25:
 dias= 30
else:
 dias= worked_days.WORK100.number_of_days

carga= contract.carga_familiar + contract.carga_familiar_maternal + contract.carga_familiar_invalida


if worked_days.WORK100.number_of_days == 0:
    result = 0
elif contract.tramo == 'a':
    result = round(((payslip.indicadores_id.asignacion_familiar_monto_a*carga) / 30) * (dias))
elif contract.tramo == 'b':
    result = round(((payslip.indicadores_id.asignacion_familiar_monto_b*carga) / 30) * (dias))
elif contract.tramo == 'c':
    result = round(((payslip.indicadores_id.asignacion_familiar_monto_c*carga) / 30) * (dias))
elif contract.tramo == 'd':
    result = 0