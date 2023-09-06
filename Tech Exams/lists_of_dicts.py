listaIDs = [
  {
    "codigoId": "00000",
    "dueDate": "9-08-2023",
    "estado": "Finalizado",
    "cartasFaltantes": True,
    "cartasFirmadas": True,
    "cantidadCambioDueDate": 1,
  },
  {
    "codigoId": "00001",
    "dueDate": "12-09-2023",
    "estado": "En Progreso",
    "cartasFaltantes": True,
    "cartasFirmadas": False,
    "cantidadCambioDueDate": 0,
  },
  {
    "codigoId": "00002",
    "dueDate": "9-05-2023",
    "estado": "Finalizado",
    "cartasFaltantes": False,
    "cartasFirmadas": False,
    "cantidadCambioDueDate": 2,
  },
  {
    "codigoId": "00003",
    "dueDate": "9-11-2023",
    "estado": "En Progreso",
    "cartasFaltantes": False,
    "cartasFirmadas": True,
    "cantidadCambioDueDate": 3,
  }
]

"""
Ejercicio 1

  Dada la siguiente lista de diccionarios de IDs, obtener los siguientes datos:
  1) cantidad de IDs finalizados con cartas firmadas
  2) cantidad de IDs finalizados con cartas faltantes
  3) cantidad de IDs finalizados
  4) cantidad de cambios de Due Dates en total
  5) cantidad de cambios de Due Dates en IDs que todavia estan en estado: En Progreso
"""


def ids_status(a_list=list):
    # Toma una lista de diccionarios con la estructura de listaIDs e imprime los status solicitados.

    ids_fin_cartas_firmadas = 0
    ids_fin_cartas_faltantes = 0
    ids_finalizados = 0
    cambios_due_dates = 0
    cambios_due_dates_ids_en_progreso = 0

    for dicc in a_list:

        cambios_due_dates += dicc["cantidadCambioDueDate"]

        if dicc["estado"] == "En Progreso":
            cambios_due_dates_ids_en_progreso += dicc["cantidadCambioDueDate"]

        if dicc["estado"] == "Finalizado":
            ids_finalizados += 1

            if dicc["cartasFirmadas"]:
                ids_fin_cartas_firmadas += 1

            if dicc["cartasFaltantes"]:
                ids_fin_cartas_faltantes += 1

    print(f"1) IDs finalizados con cartas firmadas: {ids_fin_cartas_firmadas}")
    print(f"2) IDs finalizados con cartas faltantes: {ids_fin_cartas_faltantes}")
    print(f"3) IDs finalizados: {ids_finalizados}")
    print(f"4) Cambios de Due Dates en total: {cambios_due_dates}")
    print(
        f"5) Cambios de Due Dates en IDs que todavia estan en estado: 'En Progreso': {cambios_due_dates_ids_en_progreso}")


def remover_finalizados(a_list=list):
    # Toma una lista de diccionarios de la cual remueve cada que cumpla con el criterio evaluado
    # y regresa otra lista con los mismos. Requiere asignarlo a una variable.

    lista_finalizados = []

    for dicc in a_list:
        if dicc["estado"] == "Finalizado":
            try:
                lista_finalizados.append(a_list.pop(a_list.index(dicc)))
            except ValueError:
                print("Error en el valor")
            else:
                continue

    return lista_finalizados


ids_status(listaIDs)

listaIDs_finalizados = remover_finalizados(listaIDs)

print(f"Lista IDs en progreso: {listaIDs}")

print(f"Lista IDs finalizados: {listaIDs_finalizados}")
