######################################################
# OPTENER SECUENCIALES INTERNOS

def ObtenerSecuecial(sTabla, conexion):
    sql = "SELECT * from secuenciales where secuencial = '%s' "

    resulS = conexion.execute(sql % (sTabla)).first()

    numero = str(resulS['valor'])
    secuencia = str(
        resulS['prefijo'])+('0' * (resulS['numeroceros']-len(numero)))+str(resulS['valor'])

    valor = resulS['valor'] + 1

    sql2 = "UPDATE secuenciales SET valor = %d where secuencial = '%s'"
    result2 = conexion.execute(sql2 % (valor, sTabla))

    return secuencia
