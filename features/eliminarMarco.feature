# -- FILE: features/eliminarMarco.feature
Feature: Eliminar un marco metodologico, teorico y juridico a un proyecto

    Scenario: Se elimina un marco metodologico a un proyecto
        Given: El usuario se encuentra en la vista que muestra la lista de los marcos metodologico
        When: El usuario presiona eliminar y aparece una vista que pregunte si esta seguro eliminar y presiona aceptar
        Then: Se muestra un mensaje que el marco metodologico ha sido eliminado exitosamente

    Scenario: Se elimina un marco juridico a un proyecto
        Given: El usuario se encuentra en la vista que muestra la lista de los marcos juridico
        When: El usuario presiona eliminar y aparece una vista que pregunte si esta seguro eliminar y presiona aceptar
        Then: Se muestra un mensaje que el marco juridico ha sido eliminado exitosamente

    Scenario: Se elimina un marco teorico a un proyecto
        Given: El usuario se encuentra en la vista que muestra la lista de los marcos teorico
        When: El usuario presiona eliminar y aparece una vista que pregunte si esta seguro eliminar y presiona aceptar
        Then: Se muestra un mensaje que el marco teorico ha sido eliminado exitosamente