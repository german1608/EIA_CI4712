# -- FILE: features/modificarMarco.feature
Feature: Modificar un marco metodologico, teorico o juridico a un 
    proyecto

    Scenario: Se modifica un marco metodologico a un proyecto 
        Given: El usuario se encuentra en la vista que muestra la descripcion del marco metodologico.
        When: El usuario modifica algo del texto y presiona modificar.
        Then: Se muestra un mensaje que el marco metodologico ha sido modificado exitosamente

    Scenario: Se modifica un marco juridico a un proyecto 
        Given: El usuario se encuentra en la vista que muestra la descripcion del marco juridico.
        When: El usuario modifica algo del texto y presiona modificar.
        Then: Se muestra un mensaje que el marco juridico ha sido modificado exitosamente

    Scenario: Se modifica un marco teorico a un proyecto 
        Given: El usuario se encuentra en la vista que muestra la descripcion del marco teorico.
        When: El usuario modifica algo del texto y presiona modificar.
        Then: Se muestra un mensaje que el marco teorico ha sido modificado exitosamente