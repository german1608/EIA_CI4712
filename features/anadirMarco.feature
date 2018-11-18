# -- FILE: features/anadirMarco.feature
Feature: Anadir un marco metodologico, teorico y juridico a un proyecto

    Scenario: Se agrega un marco metodologico a un proyecto
        Given: El usuario se encuentra en la vista de agregar un marco metodologico
        When: El usuario escribe el marco metodologico en el cuadro de texto de la y presiona agregar
        Then: Se muestra un mensaje que el marco metodologico se agrego exitosamente

    Scenario: Se agrega un marco juridico a un proyecto
        Given: El usuario se encuentra en la vista de agregar un marco juridico
        When: El usuario escribe el marco juridico en el cuadro de texto de la vista y presiona agregar
        Then: Se muestra un mensaje que el marco juridico se agrego exitosamente

    Scenario: Se agrega un marco teorico a un proyecto
        Given: El usuario se encuentra en la vista de agregar un marco teorico
        When: El usuario escribe el marco teorico en el cuadro de texto de la vista y presiona agregar
        Then: Se muestra un mensaje que el marco teorico se agrego exitosamente